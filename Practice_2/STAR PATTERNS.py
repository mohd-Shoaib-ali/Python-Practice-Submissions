#91. Print a Single Star (*)
print("*")

#92. Print Four Stars (****)
print("***")

#93. Print n Stars on Same Line
n=5
for i in range(n+1):
    print("*")

#94Print Square of Stars (n x n Stars)
n=5
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()

#95. Print an Increasing Triangle of Stars
n=5
for i in range(1,n+1):
    print("*"*i)

#96. Print a Right-Aligned Triangle of Stars    
n=5
for i in range(n-1,-1,-1):
    print(" "*i,"*"*(n-i))


#97. Print Stars in Even Numbers (2, 4, 6, 8, 10)
n=10
for i in range(1,n+1):
    if i%2==0:
        print("*"*i)


#98. Print Stars in Odd Numbers (1, 3, 5, 7, 9)
n=10
for i in range(1,n+1):
    if i%2!=0:
        print("*"*i)

#99.Print a Centered Pyramid of Stars
n=5

for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()    

#100. Print Numbers in an Increasing Sequence (1, 12, 123, 1234, 12345)

for i in range(1,7):
    for j in range(1,i+1):
        print(j,end=" ")
    print()