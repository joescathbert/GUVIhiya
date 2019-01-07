a = input()
x = a[::2]
y = a[1::2]
an = ""
for i in range(len(x)):
	an+=y[i]
	an+=x[i]
print(an)
