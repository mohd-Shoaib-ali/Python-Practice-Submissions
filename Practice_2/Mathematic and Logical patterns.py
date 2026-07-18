
#71.Print the squares of numbers from 1 to n.
n=int(input())
for i in range(0,n):
    print(i*i,end=" ")

#72.Print cubes of numbers from 1 to n.
n=int(input())
for i in range(0,n):
    print(i*i*i,end=" ")

#73.Print cubes of numbers from 1 to n.
n=int(input())
for i in range(0,n):
    print(i*i*i,end=" ")

#74.Find HCF (GCD) of two numbers using loops.

def hcf_loop(a, b):
    a, b = abs(a), abs(b)
    if a == 0: return b
    if b == 0: return a
    for i in range(min(a, b), 0, -1):  # start from smaller and go down
        if a % i == 0 and b % i == 0:
            return i

# example
#print(hcf_loop(54, 24))  # prints 6
#====================================
def hcf_euclid(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
# example
#print(hcf_euclid(54, 24))  # prints 6
#=====================================
import math
math.gcd(54, 24)  # returns 6
#75.Find LCM of two numbers using loops.
def lcm_loop(a, b):
    a, b = abs(a), abs(b)
    bigger = max(a, b)

    while True:
        if bigger % a == 0 and bigger % b == 0:
            return bigger
        bigger += 1

print(lcm_loop(4, 6))   # 12
print(lcm_loop(54,24)) #216

a=int(input("a: "))
b=int(input("b: "))
bigger=max(a,b)
while True:
    if bigger%a==0 and bigger%b==0:
        print(bigger)
        break
    bigger+=1

#76.Print all factors of a given number.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)

#77.Find the sum of all factors of a number.
n=int(input("N: "))
summ=0
for i in range(1,n+1):
    if n%i==0:
        summ+=i
print(summ)
