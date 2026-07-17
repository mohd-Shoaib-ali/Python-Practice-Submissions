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
