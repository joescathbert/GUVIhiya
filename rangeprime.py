a, b = [int(x) for x in input().split()]
p = [True for i in range(b+1)]
s = 2
while s**2 <= b:
    if p[s] == True:
        for i in range(s**2,b+1,s):
            p[i] = False
    s += 1
c = 0
for i in range(a,b+1):
    c += 1 if p[i] else 0
print(c)
