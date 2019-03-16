def targ(a, n, k):
    for i in range(n-1):
        for j in range(i,n):
            if a[i] + a[j] == k:
                return True
    return False
n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()][:n]
if targ(arr, n, k):
    print("YES")
else:
    print("NO")
