#61.count the number of digits in a given number

num=int(input("Enter a Number: "))
count=0
while num>0:
    dig=num%10
    count+=1
    num//=10
print(count)
#=================================
num=int(input("Enter a Number: "))
print(int(len(str(num))))

#62.print reverse of a given number
num=int(input("Enter a Number: "))
print(str(num)[::-1])
#=================================
num=int(input("Enter a Number: "))
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num//=10
print(rev)

#63.Check if given number is palindrome
num=int(input("Enter a Number: "))
temp=num
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num//=10
print("Palindrome"  if temp==rev else "Not Palindrome")

#================================================
num=int(input("Enter a Number: "))
rev=int(str(num)[::-1])

print("P" if num==rev else "NP")

#64.find the sum of digits of a number

num=int(input("Enter a Number: "))
sum=0
while num>0:
    dig=num%10
    sum+=dig
    num//=10
print(sum)

#65.Check if the number is Armstrong
num=int(input("Enter a Number: "))
temp=num
sum=0
length=int(len(str(num)))
while num>0:
    dig=num%10
    sum+=dig**length
    num//=10
print("Armstrong" if temp==sum else "Not Armstrong")


#66.check if a number is perfect number
num=int(input("Enter a Number: "))
summ=0
for i in range(1,num):
    if num%i==0:
        summ+=i
if summ==num:
    print("Perfect number")
else:
    print("Not a Perfect Number")


#67.print all prime numbers between 1 to 100
num =int(input())
for n in range(2,num+1):
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            break
    else:
        print(n,end=" ")


#68.Check is a number  prime or not

num =int(input())
for i in range(2,int(num**0.5)+1):
    if num%i==0:
        print("Not Prime")
        break
    else:
        print("Prime")


#69.Print Fibonacci series up to n terms.
n=int(input())
def print_fibonacci(n):
    a,b=0,1
    for _ in range(n):
        print(a,end=" ")
        a,b=b,a+b
print_fibonacci(n)
