n = input()
di = {}
for i in n:
    if i not in di:
        di[i] = 1
    else:
        di[i] += 1
di = [(i,j) for i,j in di.items()]
print(max(di, key=lambda x:x[1])[0])
