#Problem1:
#Given a year, determine whether the year is leap year or not, return the Boolean True, otherwise return False
def check_leap(year):
    leap = False
    if year%4 == 0 and (year%100 != 0 or year%400 ==0):
        leap = True
    return leap

year = int(input("Enter the year to check whether its leap year or not:"))
print(check_leap(year))