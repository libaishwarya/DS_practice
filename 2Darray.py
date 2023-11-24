arr = [[1,2,3],[4,5,6],[7,8,9]]
for i in arr:
    for j in i:
        print(j, end=" ")
    print()

arr = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]

sum = 0
for i in arr:
    for j in i:
        sum = sum + j
print(sum)

for i in range(0,len(arr)):
    for j in range(0, len(arr[i])):
        if i == j:
            sum = sum + arr[i][j]
print(sum)     

for i in range (1):
    for j in range (len(arr[i])):
        sum = sum + arr[i][j]
print(sum)

for i in range(0,len(arr)):
    for j in range(1):
        sum = sum + arr[i][j]
print(sum)
        
for i in range(len(arr[-1])-1,len(arr[-1])):
    for j in range(len(arr[i])):
        sum = sum+ arr[i][j]
print(sum)

for i in range(0,len(arr)):
    for j in range(len(arr[-1])-1,len(arr[-1])):
        sum = sum+ arr[i][j]
print(sum)

for i in range (0,len(arr)): 
    for j in range (len(arr[i])):
        if i ==0 and i == len(arr):
            sum = sum + arr[i][j]
print (sum)

for i in range (0,len(arr)):
        
        for j in range (0, len(arr[i])):
            if i == len(arr):
                sum = sum + arr[i][j]
                print (sum) 
  
sum = 0
for i in range(0,len(arr)):
    if i == 0 or i == len(arr)-1:
        j = range(0,len(arr[i]))
    else:
        j = [0, len(arr[i])-1]
    for k in j:
        sum = sum + arr[i][k]
    
print(sum)

arr = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
sum = 0

i = len(arr)-1
for i in range(0,len(arr)):
    if i == len(arr)-1:
        j = range(0,len(arr[i]))
    else:
        j = [0]
    for k in j :
        sum = sum +arr[i][k]
        
print(sum)

        
        
