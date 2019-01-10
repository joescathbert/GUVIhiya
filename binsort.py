n = int(input())
arr = [(int(x), sum(list(map(int, bin(int(x))[2:])))) for x in input().split()]
arr.sort(key=lambda x:(x[1],x[0]),reverse=True)
for i in arr:
    print(i[0])
