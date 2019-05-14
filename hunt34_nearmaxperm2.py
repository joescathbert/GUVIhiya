n = list(map(int, list(input())))
m = max(n)
ind = len(n) - n[::-1].index(m) - 1
for i in range(-1, -len(n)-1, -1):
    r = n.copy()
    r[i], r[ind] = r[ind], r[i]
    if int("".join(list(map(str, r)))) > int("".join(list(map(str, n)))):
        print(int("".join(list(map(str, r)))))
        break
else:
    print("impossible")
