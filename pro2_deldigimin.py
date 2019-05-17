
def recur(digi, temp, arr, m, n, k, mi):
    if m == n - 1:
        nr = arr[:k]
        temp.append(nr)
        dr = digi.copy()
        for i in nr:
            if i in nr: 
                dr[i] = 'a'
        dr = [i for i in dr if i != 'a']
        no = int("".join(list(map(str,dr))))
        if no < mi:
            mi = no
        return temp, mi
    else:
        for i in range(m,n):
            if arr[m] != arr[i] or i == m:
                ar2 = arr.copy()
                ar2[i], ar2[m] = ar2[m], ar2[i]
            if ar2[:k] not in temp:
                temp, mi = recur(digi, temp, ar2, m+1, n, k, mi)
        return temp, mi

arr, k = input().split()
k = int(k)
if k == 0: print(int(arr))
arr = list(map(int, arr))
if k != 0:
    print(recur(arr, [], [x for x in range(len(arr))], 0, len(arr), k, int("".join(list(map(str,arr[:k+1])))))[1])
