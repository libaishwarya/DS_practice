n = 6
for i in range(1,n+1):
    for j in range(0,(n-i)):
        print(" ", end =" ")
    for k in range(0,i):
        print(" *  ", end = "")
    print ('\n')
for i in reversed(range(0,n)):
    for j in range(0,n-i):
        print("  ", end ="")
    for k in range (0,i):
        print("  *", end =" ")
    print('\n')