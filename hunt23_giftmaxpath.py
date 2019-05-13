def recur(temp,marr,arr,m,n,sa):
  if m == n - 1:
    j, k = 0, 0
    su = marr[j][k]
    for i in arr:
      if i == 'r': k+=1
      if i == 'b': j+=1
      su += marr[j][k]
    if su > sa: sa = su
    temp.append(arr)
    return temp, sa
  else:
    for i in range(m,n):
      if arr[m] != arr[i] or i == m:
        ar2 = arr.copy()
        ar2[i], ar2[m] = ar2[m], ar2[i]
        if ar2 not in temp:
          temp, sa = recur(temp, marr, ar2, m+1, n, sa)
    return temp, sa

arr = [] 
m, n = list(map(int, input().split()))
for i in range(m):
  arr.append([int(x) for x in input().split()])
ar = (['r']*(n-1)) + (['b']*(m-1))
if m == 1 and n == 1:
  print(arr[0][0])
else:
  a,b = recur([],arr,ar,0,len(ar),0)
  print(b)
