def recur(temp,arr,m,n):
    if m == n - 1:
        temp.append(arr)
        return temp
    else:
        for i in range(m,n):
            if arr[m] != arr[i] or i == m:
                ar2 = arr.copy()
                ar2[i], ar2[m] = ar2[m], ar2[i]
            if ar2 not in temp:
                temp = recur(temp, ar2, m+1, n)
        return temp


digi = input()
a = [int("".join(list(map(str,i)))) for i in recur([],list(map(int,list(digi))),0,len(digi))]
a.sort()
if (a.index(int(digi))+1) >= len(a):
    print('impossible')
else:
    print(a[a.index(int(digi))+1])
    
