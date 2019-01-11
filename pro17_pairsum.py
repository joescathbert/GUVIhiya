n, k = map(int,input().split())
arr = [int(x) for x in input().split()]
f = False
for i in range(0,n-1):
    for j in range(i+1,n):
        if arr[i] + arr[j] == k:
            print("yes")
            f = True
            break
    if f:
        break
else:
    print("no")
