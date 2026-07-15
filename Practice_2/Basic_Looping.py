#51.Print numbers from 1 to 10.
for i in range(0,10):
    print(i)

#52.print all even numbers from 1 and 100
for i in range(1,100+1):
    if i%2==0:
        print(i)

#53.print all odd numbers from 1 and 100
for i in range(1,100+1):
    if i%2!=0:
        print(i)

#54.print numbers down from 10 to 1
for i in range(10,1-1,-1):
	print(i)


#55.print the table of given number
n=int(input("Enter a Number: "))
for i in range(1,10+1):
    print(f"{n} * {i}  = {n*i}")

#56.print the sum of first n natural numbers
n=int(input("Enter a Number: "))
print(int(n*((n+1)/2)))

