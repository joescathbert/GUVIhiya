n = int(input())
arr = [int(x) for x in input().split()]
mem = []
for a in arr:
    if a not in mem:
        mem.append(a)
    else:
        print(a)
        break
else:
    print("unique")
