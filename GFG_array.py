#sum of series
n = 5
sum = 0
for i in range(1,n+1):
    #     sum = sum + i
    # print(sum)

    m = int(n*(n+1)/2)
print (m)
#========================================
#value equal to index
arr = [None,15,2,45,12,7]
arr = [None,1,3,45,12,7]
for i in range(1,len(arr)):
    if i == int(arr[i]):
        print(i)
#========================================
#sum of arrray element

n = 6
arr = [1,3,45,12,7,1]
sum = 0
for i in range(len(arr)):
    sum = sum + arr[i]
print(sum)

  