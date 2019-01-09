n = int(input())
arr = input().split()
dic = {}
for i in arr:
	if i not in dic:
		dic[i] = 1
	else:
		dic[i] += 1
arr = [(i,j) for i,j in dic.items()]
print(int(min(arr, key=lambda x:x[1])[0]))
