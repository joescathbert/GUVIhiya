n = int(input())
arr1 = [int(x) for x in input().split()]
arr2 = [x*n for x in range(1,n+1)]
print(len(set(arr1).intersection(set(arr2))))
