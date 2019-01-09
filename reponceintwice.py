num = int(input())
a = input().split()
diction = {}
for k in a:
	if k not in diction:
		diction[k] = 1
	else:
		diction[k] += 1
a = [(x,y) for x,y in diction.items()]
print(int(min(a, key=lambda x:x[1])[0]))
