n = 5
for i in range (0,n+1):
    for j in range (0,i):
        print(" *",end = " ") 
    print('\n')

for i in range(0,n+1):
    for j in range(0,n-i):
        print(" * ", end = " ")
    print('\n')
    
for i in range (0,n):
    for j in range(n-(i+1)):
        print( " ", end = " ")
    k = n-j
    for k in range (n):
        print(" * ", end=" ")
    print('\n')

n = 5
for i in range(0,n):
    for j in range(1, n-i):
        print(" ", end="")
    for k in range(0, i + 1):
        print(" *", end="")
    print()

n = 5
for i in range(0,n):
    for j in range(1, n-i):
        print(" ", end=" ")
    for k in range(0, i + 1):
        print("*", end=" ")
    print()
   