import datetime
import time
import winsound

print("-------Alarm Clock-------")

alarm_hour = int(input("Enter Hour:"))
alarm_minute = int(input("Enter Minute:"))
am_pm = input("Enter AM or PM:").upper()
while True:
    current_time = datetime.datetime.now()
    # %I is used to get the hour in 12-hour format, %p is used to get AM or PM
    current_hour = int(current_time.strftime("%I"))
    current_minute = current_time.minute
    current_am_pm = current_time.strftime("%p")

    print("Current Time: ", current_time.strftime("%I:%M:%S %p"))

    if current_hour == alarm_hour and current_minute == alarm_minute and current_am_pm == am_pm:
        print("Wake Up!")
        winsound.Beep(1000, 4000)
        break
    time.sleep(1)
