#1.Take a number and print it is positive or negative or zero
n=int(input())
if n>=1:
    print("Positive")
elif n==0:
    print("Zero")
else:
    print("Negative")
#2.check if a number is even or odd
n=int(input())
if n%2==0:
    print("Even")
else:
    print("Odd")
#3.check if a number is divisible by zero
n=int(input())
print("Yes" if n%5==0 else "No")

#4.check if a number divisible by 3 & 5
n=int(input())
print("Yes" if n%5==0 and n%3==0 else "No")

#5.check if given number is leap year
year=int(input())

if year%400==0 and (year%4==0 or year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#6.Take two numbers and print large one
first = 20
second = 35
if first > second:
    print(first)
else:
    print(second)

#7.Take three numbers and print large one
a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
print("Max Value:",max(a,b))
#______________________________________
first = 20
second = 35
third=40
if first > second and first >third:
    print(first)
elif second >first and second >third:
    print(second)
else:
    print(third)
#--------------------------------------
first = 20
second = 35
third = 12
largest = first
if second > largest:
    largest = second
if third > largest:
    largest = third
print("Largest = " + str(largest))

#8.Take a temperature value and print "Cold", "Warm", or "Hot" using range conditions.
temperature = 31
if temperature < 15:
    print("Cold")
elif temperature <= 30:
    print("Warm")
else:
    print("Hot")

#9.Take a character and check if it's a vowel or consonant.
alp=str(input())
lower=alp.lower()
if lower=="a" or lower=="e" or lower=="i" or lower=="o" or lower=="u":
    print("Vowel")
else:
    print("conconent")
#============================================================
def isVowel(ch):
    lower = ch.lower()
    return lower == 'a' or lower == 'e' or lower == 'i' or lower == 'o' or lower == 'u'

def main():
    ch = 'e'
    if ch.isalpha():
        if isVowel(ch):
            print("Vowel")
        else:
            print("Consonant")
    else:
        print("Not an alphabet")


if __name__ == "__main__":
    main()

#10.Take a character and check whether it's uppercase, lowercase, a digit, or a special character.
ch = 'A'
if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")

