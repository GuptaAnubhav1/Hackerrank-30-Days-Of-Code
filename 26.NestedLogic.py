import os
import sys
import math
import datetime

day,month,year = [int(x) for x in input().split(' ')]
day1,month1,year1 = [int(x) for x in input().split(' ')]
fine = 0
if (year) > (year1):
    fine += 10000
elif (year) < (year1):
    fine += 0
elif (year) == (year1):
    if (month) < (month1):
        fine += 0
    elif (month) == (month1):
       if (day) <= (day1):
        fine += 0
       elif (day) > (day1):
        fine += 15 *(day - day1)
    elif (month) > (month1):
        fine += 500 *(month - month1)
print(fine)
