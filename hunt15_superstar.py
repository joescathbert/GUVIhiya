n = int(input())
arr = [int(x) for x in input().split()]
star = []
for i in range(len(arr)-1):
    if max(arr[i+1:]) < arr[i]:
        star.append(arr[i])
star.append(arr[len(arr) - 1])
print(" ".join(list(map(str, star))))
print(max(arr))
