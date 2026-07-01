import time
Hours = int(input("Enter Hours: "))
Minutes = int(input("Enter Minutes: "))
Seconds = int(input("Enter Seconds: "))
Total_time = Hours * 3600 + Minutes * 60 + Seconds
while Total_time > 0:
    print(Total_time)
    time.sleep(1)
    Total_time -= 1
print("Time's Up")