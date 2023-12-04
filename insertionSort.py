arr = [6,3,9,2,4,3,0,1,4,8]

for i in range(len(arr)-1):
    j = i+1
    while(arr[j]<arr[i]):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        if (i > 0):
            j = j-1
            i = i -1
        else:
            break
print(arr)