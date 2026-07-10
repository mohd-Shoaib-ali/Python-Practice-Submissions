#31.Take a character and check if it is a letter, a digit, or neither.
ch=str(input())
if ch.isalpha():
    print("Letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Neither")

#32.Take a number and print "Fizz" if divisible by 3, "Buzz" if divisible by 5, and "FizzBuzz" if divisible by both.
num=int(input())
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print("Not Divisible by 5 or 3")

#33.Take three numbers and print the median value (neither maximum nor minimum).
a = 12
b = 5
c = 20
median = 0
if (a >= b and a <= c) or (a >= c and a <= b):
    median = a
elif (b >= a and b <= c) or (b >= c and b <= a):
    median = b
else:
    median = c
print("Median = " + str(median))


#34.Take 24-hour time (hours and minutes) and print whether it is AM or PM.

h = int(input("Enter hour (0-23): "))
m = int(input("Enter minutes (0-59): "))

if 0 <= h <= 11:
    print("AM")
elif 12 <= h <= 23:
    print("PM")
else:
    print("Invalid time")

#35.Take income and age, and check if eligible for tax (age > 18 and income > 5 L).

age=int(input("Age:"))
income=int(input("Income:"))
if age>=18 and income>=500000 :
    print("Eligible for tax")
else:
    print("Not Eligible")

#36.Take two numbers and check if both are positive and their sum is less than 100.

first = 30
second = 40
if first > 0 and second > 0 and first + second < 100:
    print("Condition satisfied")
else:
    print("Condition not satisfied")

#===============================================

a=int(input("A:"))
b=int(input("B:"))
if (a>1 and b>1):
    print("yes both are possitive")
    if (a+b)<100:
        print("yes less than 100")
    else:
        print("Greater than 100")
else:
    print("Numbers are not positive")


#37.Take a single digit (0-9) and print its word form ("Zero" to "Nine").

digit = 7
words = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}
if digit >= 0 and digit <= 9:
    print(words[digit])
else:
    print("Invalid digit")

#38.Take a day number (1-7) and print the corresponding day name.

day = 3
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
if 1 <= day <= 7:
    print(days[day - 1])
else:
    print("Invalid day")
   

#Take a weekend number(1-7) and determine if it is a weekend or not

num=int(input("Week Nummber Mon=1 Sun=7:"))
if num==6 or num==7:
    print("Weekend")
elif num<=5:
    print("week day")
else:
    print("Valid Number")



#39.Calculate electricity bill based on units using slab rates.

units = 150
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
print("Bill = " + str(bill))


#40.Take a password string and check basic rules (length >= 8 and contains at least one digit).
password = "Code123not "
hasDigit = False
hasUpper = False
hasLower = False
hasSpecial = False
for i in range(0, len(password)):
    ch = password[i]
    if ch.isdigit():
        hasDigit = True
    elif ch.isupper():
        hasUpper = True
    elif ch.islower():
        hasLower = True
    else:
        hasSpecial = True
    if len(password) >= 8 and hasDigit and hasUpper and hasLower and hasSpecial:
        print("Valid password")
    else:
        print("Invalid password")

