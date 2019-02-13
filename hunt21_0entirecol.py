m, n = map(int, input().split())
arr = []
for x in range(m):
  arr.append([v for v in input().split()][:n])
for i in range(m):
  if '0' in arr[i]:
    arr[i] = ['0']*n
  print(" ".join(arr[i]))
