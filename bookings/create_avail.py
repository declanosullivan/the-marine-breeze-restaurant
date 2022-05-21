from datetime import datetime, timedelta
import time

print(datetime.now().hour)
start_time = '9:00'
end_time = '22:00'
time_slots = []
s_time = datetime.strptime(start_time, '%H:%M')
e_time = datetime.strptime(end_time, '%H:%M')
while s_time <= e_time:
    
    _e_time = s_time + timedelta(minutes=120)
    time_slots.append((s_time, _e_time))
    s_time += timedelta(minutes=120)
    

print(time_slots)
# start_date = datetime.today()
# end_date = start_date + timedelta(days=30)
# # print(start_date, end_date)
# # loop every day for the next 30 days
# # get all table objects
# # loop over every table object
# # loop over each slot
# # create TableAvail objects for each table
# for x in range(0, 30):
#     start_date = start_date + timedelta(days=1)
    
#     print(start_date)
