n = int(input())
arr = [int(x) for x in input().split()]
ma = arr[0]
for i in range(0,n):
  for j in range(i+1,n+1):
    t = sum(arr[i:j])
    if ma < t:
      ma = t
print(ma)
