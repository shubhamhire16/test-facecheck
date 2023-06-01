import csv
import io
from datetime import datetime, timedelta

from Home import st
from Home import face_rec

st.set_page_config(page_title='Reporting', layout='wide')
st.subheader('Reporting')

# Retrieve logs data and show in Report.py
# extract data from Redis list
name = 'attendance:logs'
def load_logs(name, end=-1):
    logs_list = face_rec.r.lrange(name, start=0, end=end)  # extract all data from the Redis database
    return logs_list

# Function to convert logs to CSV file
def convert_to_csv(logs):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(logs)
    return output.getvalue()

# Retrieve the data from Redis Database
with st.spinner('Retrieving Data from Redis DB ...'):
    redis_face_db = face_rec.retrive_data(name='academy:register')

# Tabs to show the info
tab1, tab2 = st.tabs(['Registered Data', 'Logs'])

with tab1:
    if st.button('Refresh Data'):
        st.dataframe(redis_face_db[['Name', 'Role', 'roll_num', 'stu_class']])

with tab2:
    logs = load_logs(name=name)
    log_data = [log.decode('utf-8').split('@') for log in logs]  # Split elements with "@"
    print(log_data)
    # Dropdown to select time period
    time_period = st.selectbox('Select time period', ['Last 1 hour', 'Last 2 hours', 'Last 3 hours'])
    now = datetime.now()
    
    if time_period == 'Last 1 hour':
        filter_time = now - timedelta(hours=1)
    elif time_period == 'Last 2 hours':
        filter_time = now - timedelta(hours=2)
    elif time_period == 'Last 3 hours':
        filter_time = now - timedelta(hours=3)
        
    filtered_logs = [log for log in log_data if datetime.strptime(log[2], '%Y-%m-%d %H:%M:%S.%f') >= filter_time]
    
    if filtered_logs:
        log_data_with_headers = [["Name", "Role", "Date"]] + filtered_logs
        
        if st.button('Refresh Logs'):
            # Convert logs to CSV and download
            csv_data = convert_to_csv(log_data_with_headers)
            st.download_button('Download CSV', data=csv_data, file_name='logs.csv', mime='text/csv')
            
            # Display logs in a table
            st.table(log_data_with_headers)
    else:
        if st.button('Refresh Logs'):
            st.write('No logs available within the selected time period')
        else:
            st.write('No logs available within the selected time period')
