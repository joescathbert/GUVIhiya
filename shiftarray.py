n, k = map(int, input().split())
arr = [int(x) for x in input().split()]
ar = [arr[(i+(n-k))%n] for i in range(len(arr))]
for i in ar:
    print(i,end=" ")

