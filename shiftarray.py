n, k = map(int, input().split())
arr = [int(x) for x in input().split()]
print([arr[(i+(n-k))%n] for i in range(len(arr))])
