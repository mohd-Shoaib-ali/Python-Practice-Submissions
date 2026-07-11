#41.Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the origin.

x=int(input())
y=int(input())
if x==0 and y==0:
    print("Lies on origin")
elif y==0 :
    print("Lies on X-axis")
elif x==0 :
    print("Lies on Y-axis")
else:
    print("Not on any  axis")

#42 Take three numbers and check if they can form a Pythagorean triplet.
a = 3
b = 4
c = 5
if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
    print("Pythagorean triplet")
else:
    print("Not a Pythagorean triplet")

 #43.Take day and month and check if it forms a valid calendar date (ignoring leap years).
days=int(input())
month=int(input())

day_in_month={
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}
if month in day_in_month and days>=1 and days<=day_in_month[month]:
    print("correct")
else:
    print("Wrong")

#=========================================================================================

day = int(input())
month = int(input())

day_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

if month in day_in_month and 1 <= day <= day_in_month[month]:
    print("Correct")
else:
    print("Wrong")

#44.Take time (hours and minutes) and print the smaller angle between the hour and minute hands.

hours = int(input())
minutes = int(input())

# Calculate angles
hour_angle = (hours % 12) * 30 + minutes * 0.5
minute_angle = minutes * 6

# Find the smaller angle
angle = abs(hour_angle - minute_angle)
smaller_angle = min(angle, 360 - angle)

print(smaller_angle)

#45: : Take three numbers and check if they are in arithmetic progression.

a = 4
b = 8
c = 12
if b - a == c - b:
    print("Arithmetic progression")
else:
    print("Not an arithmetic progression")

#46:Take three numbers and check if they are in geometric progression.
a = int(input())
b = int(input())
c = int(input())

if b * b == a * c:
    print("Geometric Progression")
else:
    print("Not a Geometric Progression")

# 47:Take a 3-digit number and check if the sum of the first and last digit equals the middle digit.
num=int(input())
first=num//100
sec=(num//10)%10
third=num%10

if first + third==sec:
    print("Yes")
else:
    print("NO")

#48.Take an integer (1-9999) and check if the sum of its digits is greater than the product of its digits.

num=int(input())
total=0
def sum_of_nums(num):
    total=0
    while num>0:
        val=num%10
        total+=val
        num=num//10
    return total


def prod_of_nums(num):
    prod=1
    while num>0:
        val=num%10
        prod*=val
        num=num//10
    return prod
summ= sum_of_nums(num)
product =prod_of_nums(num)
if summ > product:
    print("Digit sum is greater")
else:
    print("Digit product is greater or equal")


#49.Take two dates (day and month) and determine which one comes first in the calendar.
day1 = 12
month1 = 5
day2 = 10
month2 = 6
if month1 < month2 or (month1 == month2 and day1 < day2):
    print("First date comes first")
elif month1 == month2 and day1 == day2:
    print("Both dates are same")
else:
    print("Second date comes first")

#50.Take a year and print the corresponding century (e.g., "19th century", "20th century").
year = 1998
century = (year + 99) // 100
print(str(century) + "th century")