import datetime
from playsound import playsound 
print("*****   ALARM   *****")
alarmhour = int(input("Enter Hour     :  "))
alarmmin = int(input("Enter Minutes  :  "))
alarmam = input("am/pm          :  ")

if alarmam == "pm":
    alarmhour+=24

while True:
    if alarmhour == datetime.datetime.now().hour and alarmmin == datetime.datetime.now().minute:
        print("*****  Ringing Alarm  *****")
        playsound("Alarm")
        break