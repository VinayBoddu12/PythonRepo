"""
Task

You are given a date. Your task is to find what the day is on that date.

Sample Input:
08 05 2015

Sample Output:
WEDNESDAY
"""

import calendar as c

def finding_day(month, day, year):
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    day_of_week = c.weekday(year, month, day)
    return days[day_of_week]