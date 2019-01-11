def merge(x,y):
    temp = []
    i ,j = 0,0
    while i != len(x) and j != len(y):
        if x[i] < y[j]:
            temp.append(x[i])
            i += 1
        else:
            temp.append(y[j])
            j += 1
    if i == len(x):
        return temp+y[j:]
    else:
        return temp+x[i:]
    
n = int(input())
arr = [[int(x) for x in input().split()] for i in range(n)]
temp = []
for i in arr:
    temp = merge(temp,i)
print(" ".join(map(str,temp)))
