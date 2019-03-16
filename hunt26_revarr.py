n = int(input())
arr = [int(x) for x in input().split()]
print("->".join(list(map(str, arr[::-1]))))
