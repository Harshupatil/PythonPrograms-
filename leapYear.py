'''
The year which is evenly divided by 4 is a leap year. But this is not true in the case of century years
if the year is evenly divided by 100. And also by 400 in this case we called it as a leap year.
The following program return true if year is leap and false if year is not leap.  
'''
def is_leap(year):
    leap = False
    if year%100 == 0:
        if year%400 == 0:
            leap = True
    elif year%4 ==0:
        leap = True
    return leap

year = int(input())
print(is_leap(year))