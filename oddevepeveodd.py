n = int(input())
arr = [int(x) for x in input().split()]
for i in range(len(arr)):
    if (i % 2 == 0 and arr[i] % 2 == 1) or (i % 2 == 1 and arr[i] % 2 == 0):
        print(arr[i],end=' ')
