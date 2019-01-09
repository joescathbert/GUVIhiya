n = int(input())
arr = [int(x) for x in input().split()]
dic = {}
for a in range(len(arr)):
    if arr[a] not in dic:
        dic[arr[a]] = [1,a]
    else:
        dic[arr[a]][0] += 1
arr = [(i, j[1]) for i,j in dic.items() if j[0] > 1]
if len(arr) == 0:
    print("unique")
else:
    print(min(arr, key=lambda x:x[1])[0])
