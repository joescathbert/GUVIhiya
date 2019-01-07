a, b = [list(x) for x in input().split()]
a[0], b[0] = a[0].upper(), b[0].upper()
print("".join(a),"".join(b))
