#sum of series
# n = 5
# sum = 0
# for i in range(1,n+1):
#         sum = sum + i
#     print(sum)

#     m = int(n*(n+1)/2)
# print (m)
# #========================================
# #value equal to index
# arr = [None,15,2,45,12,7]
# arr = [None,1,3,45,12,7]
# for i in range(1,len(arr)):
#     if i == int(arr[i]):
#         print(i)
# #========================================
# #sum of arrray element

# n = 6
# arr = [1,3,45,12,7,1]
# sum = 0
# for i in range(len(arr)):
#     sum = sum + arr[i]
# print(sum)
# #=======================================
# #print alternative elements

# arr = [1,23,3,4,5,6,7,8,9,12,13]
# for i in range (0,len(arr)):
#     if i == 0:
#         print(arr[i], end = " ")
#     elif i % 2==0:
#         print(arr[i], end = " ") 

## ========================================
## Palindromic Array
# n = 5
# arr = [111, 222 ,333, 444, 555]

# for i in range (0,n):
# #         if arr[i]%11 == 0 | arr[i] == [1,9]:
# #             a = 1
# #         else :
# #             a = 0
#     if arr[i] % 11 ==0:
#         print("1")
#     else:
#         print("0")
# =========================================
sum of array:
n = 5
arr = [111, 222 ,333, 444, 555]
sum = 0
for i in range(n):
    
    sum = sum + arr[i]
print(sum)
=========================================
count of smaller element:
n = 6
arr = [1,2,4,5,8,10]
x = 9
def countOfElements( a, n, x):
    m = []
    for i in range (0,n):
        if a[i] <= x:
            m.append(a[i])
    return len(m)
===========================================
find index
class Solution:
    def findIndex (self,a, N, key ):
        fIndex = -1
        for i in range(0, N):
            if a[i] == key:
                fIndex = i
                break
        if fIndex == -1:
            # handle no element existst
            return [-1, -1]
    
        bIndex = -1
        for i in reversed(range(0,N)):
            if a[i] == key:
                bIndex = i
                break
    
        return [fIndex, bIndex]
            
