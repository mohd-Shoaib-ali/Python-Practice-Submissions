#11.Take three sides and check if they form a valid triangle.
a=2
b=2
c=2
print("yes" if a+b>c and b+c>a and c+a>b else "No")


#12.If the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene.
a=3
b=2
c=4
if a+b>c and b+c>a and c+a>b:
    if a==b==c:
        print("equilateral")
    elif a==b or b==c or c==a:
        print("isosceles")
    else:
        print("scalene")
else:
    print("Not a Triangle")

 #13: : Take marks (0-100) and print the corresponding grade (A/B/C/D/F).

marks = 82
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")



#14.Check if one of two given numbers is a multiple of the other.
first = 12
second = 36
if first != 0 and second % first == 0:
    print("Second is a multiple of first")
elif second != 0 and first % second == 0:
    print("First is a multiple of second")
else:
    print("No number is a multiple of the other")

#15: : Take the hour of the day (0-23) and print "Good Morning", "Good Afternoon", "Good Evening", or "Good Night".
hour = 16
if hour >= 5 and hour < 12:
    print("Good Morning")
elif hour >= 12 and hour < 17:
    print("Good Afternoon")
elif hour >= 17 and hour < 21:
    print("Good Evening")
else:
    print("Good Night")

#16.Check voting eligibility for a given age (18+).
age = 19
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


#17. Take two numbers and determine whether both are even, both are odd, or one iseven and one is odd.
a=int(input())
b=int(input())

if a%2==0 and b%2==0:
    print("Both are Even")
elif a%2!=0 and b%2!=0:
    print("Both are Odd")
else:
    print("One even One Odd")

#18.Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’.

ch=str(input())

if ch>="a" and ch<="m":
    print("Between a and m")
elif ch>="n" and ch<="z":
    print("Between m and z")
else:
    print("Not a lowerCase")



#19.Take a day number (1–7) and print the corresponding day name.
n=int(input("Enter a day Number: "))
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

if n>=1 and n<=7:
    print(days[n-1])
else:
    print("Enter a valid  day number")


#20.Take a month number (1–12) and print the number of days in that month (ignore leapyears).
month_no=int(input("Enter Month Number: "))
dic={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
if month_no in dic:
    print(dic[month_no])
else:
    print("Enter a valid Monnth")