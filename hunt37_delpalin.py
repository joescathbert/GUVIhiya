n = input()
if len(n) % 2 == 0:
    print("NO")
else:
    if  n[len(n)//2 -1 ::-1] == n[len(n)//2 + 1:]:
        print("YES")
    else:
        print("NO")
