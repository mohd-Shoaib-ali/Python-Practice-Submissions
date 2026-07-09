#21.Take a 3-digit number and check if all digits are distinct.
number = 427
hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10
if hundreds != tens and tens != ones and hundreds != ones:
    print("All digits are distinct")
else:
    print("Digits are not distinct")

#22.Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither

num=int(input())
first=num//100
middle=(num//10)%10
last=num%10

if middle>first and middle>last:
    print("Largest")
elif middle<first and middle<last:
    print("Smallest")
else:
    print("Neither")v

#23.Take a 4-digit number and check if the first and last digits are equal.

number = 4554
firstDigit = number // 1000
lastDigit = number % 10
if firstDigit == lastDigit:
    print("First and last digits are equal")
else:
    print("First and last digits are not equal")

#24.Check whether a given integer is single-digit, double-digit, or multi-digit.

num=int(input())
strr=len(str(num))

if strr==1:
    print("Single-digit")
elif strr==2:
    print("Double-digit")
else:
    print("Multi-digit")

#==============================
number = 87
value = abs(number)
if value <= 9:
    print("Single-digit")
elif value <= 99:
    print("Double-digit")
else:
    print("Multi-digit")

#25.Check if a number is a multiple of 7 or ends with 7.
num=int(input())
if num%7==0 or num%10==7:
    print("yes")
else:
    print("No")


#26.Take coordinates (x, y) and determine which quadrant the point lies in.
x = -4
y = 6
if x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
elif x > 0 and y < 0:
    print("Quadrant IV")
else:
    print("Point lies on an axis or origin")


#27. Check if an amount can be evenly divided into 2000, 500, and 100 currency notes.

amount = 7600
notes2000 = amount / 2000
amount %= 2000
notes500 = amount / 500
amount %= 500
notes100 = amount // 100
amount %= 100
if amount == 0:
    print("2000: " + str(notes2000) + ", 500: " + str(notes500) + ", 100: " + str(notes100))
else:
    print("Amount cannot be fully divided into these notes")


#28.Check if a number lies within the range [100, 999].

num=int(input())
if num>=100 and num<=999:
    print("Lies in the range")
else:
    print("Not lies in the range")


#29.Take two angles of a triangle and compute the third angle.

first_angle=int(input())
second_angle=int(input())

print("Third_angle:",180-(first_angle+second_angle))


#30.Check whether a number is a perfect square (without using the square root function).

num=int(input())

i=0
while  i*i<num:
    i+=1
if i*i==num:
    print(num, " Square root")
else:
    print("Not a Square root")
