n = int(input())
ar = [int(x) for x in input().split()]
ar = [[ar[x],x] for x in range(len(ar))]
while len(ar) != 1:
  ar = [ar[i] for i in range(1,len(ar),2)]
print(ar[0][1])
