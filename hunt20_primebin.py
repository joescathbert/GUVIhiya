def prime(n):
  if n < 2:
    return False
  for i in range(2,int(n**(1/2))+1):
    if n % i == 0:
      return False
  else:
    return True
r, s = map(int,input().split())
print(len([x for x in range(r,s+1) if prime(len([y for y in bin(x) if y == '1']))])) 
