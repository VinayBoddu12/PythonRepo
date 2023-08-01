import datetime

def call():
    date = str(input())
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day=datetime.datetime.strptime(date,"%d %m %y").weekday()
    print(days[day])