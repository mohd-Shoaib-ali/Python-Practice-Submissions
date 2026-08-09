#1. Print a Single Star (*)
print("*")

#2. Print Four Stars (****)
print("***")

#3. Print n Stars on Same Line
n=5
for i in range(n+1):
    print("*")

#4Print Square of Stars (n x n Stars)
n=5
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()

#5. Print an Increasing Triangle of Stars
n=5
for i in range(1,n+1):
    print("*"*i)

#6. Print a Right-Aligned Triangle of Stars    
n=5
for i in range(n-1,-1,-1):
    print(" "*i,"*"*(n-i))


#7. Print Stars in Even Numbers (2, 4, 6, 8, 10)
n=10
for i in range(1,n+1):
    if i%2==0:
        print("*"*i)


#8. Print Stars in Odd Numbers (1, 3, 5, 7, 9)
n=10
for i in range(1,n+1):
    if i%2!=0:
        print("*"*i)