a, b = list(map(int, input().split()))
c = 0
while a - b >= 0:
    c += 1
    a -= b
print(c)
