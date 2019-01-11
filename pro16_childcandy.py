n = int(input())
arr = [int(x) for x in input().split()]
dic = {}
for a in arr:
    dic[a] = 1 if a not in dic else dic[a] + 1
arr = [[i,j] for i,j in dic.items()]
arr.sort(key=lambda x:x[0])
print(n + sum([arr[i][1]*i for i in range(len(arr))]))
