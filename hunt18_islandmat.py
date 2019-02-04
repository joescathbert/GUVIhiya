n = int(input())
arr = [[0]*(n+2),[0]*(n+2)]
c = 0
for i in range(n):
  arr.insert(-1, [0]+[int(x) for x in input().split()]+[0])
for i in range(1, n+1):
  for j in range(1, n+1):
    if arr[i][j] == 1 and [[[arr[i-1][r],arr[i][r],arr[i+1][r]] for r in range(j-1,j+2)]] == [[[0, 0, 0], [0, 1, 0], [0, 0, 0]]]:
      c += 1
print(c)
