a = [1,2,3,4,2,3,1,2]

def getCount(arr):
    m = {}
    for v in arr:
        if v in m.keys():
            m[v]= m[v] + 1
        else:
            m[v] = 1
            
    return m


def getIndex(arr):
    m = {}
    for i in range(0,len(arr)):
        if arr[i] in m.keys():
            m[arr[i]].append(i)
        else:
            m[arr[i]] = [i]
    return m
            
print(getCount(a))
print(getIndex(a))

            
