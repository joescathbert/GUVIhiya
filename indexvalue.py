n = int(input())
a = [int(x) for x in input().split()]
an = []
for i in range(len(a)):
    if i == a[i]:
        an.append(i)
for i in an:
    print(i,end=" ")
