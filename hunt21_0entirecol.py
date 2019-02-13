m, n = map(int, input().split())
arr = []
r = []
c = []
for x in range(m):
  arr.append([v for v in input().split()][:n])
for i in range(m):
  for j in range(n):
    if arr[i][j] == '0':
      if i not in r: r.append(i)
      if j not in c: c.append(i)
arr = [arr[i][j] if i not in r and j not in c else '0' for i in range(m) for j in range(n)]
for i in range(m):  
  print(" ".join(arr[i]))
