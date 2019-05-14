n = input()
if len(n) % 2 == 0:
    print("NO")
else:
    if n[0:len(n)//2] == n[(len(n)//2) + 1:]:
        print("YES")
    else:
        print("NO")
