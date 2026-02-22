import datetime

date = datetime.date(2025, 1, 2) #This will output 2025-01-02
today = datetime.date.today() #It will return the date of today

time = datetime.time(12,30,0)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %m-%d-%Y") #Add this if you want to edit the time

target_datetime = datetime.datetime(2020, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")

print(f"Past date: '{date}'")
print(f"Today's date: '{today}'")
print(f"Some day time {time}")
print(f"Time now '{now}'")
