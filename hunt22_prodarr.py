n = int(input())
a = [int(x) for x in input().split()]
prod = 1
for i in range(n):
    prod *= a[i]
out = [prod//i for i in a]
print(' '.join(list(map(str, out))))
