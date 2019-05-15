n, e = list(map(int, input().split()))
arr = [input().split() for i in range(e)]
pa = []
c = 0
grandpa = input()
for i in arr:
    if i[0] == grandpa:
        pa.append(i[1])
for i in arr:
    if i[0] in pa:
        c += 1
print(c)
