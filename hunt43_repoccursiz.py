import re
st = input()
arr = re.findall('([a-z]+)([0-9]+)', st, re.I)
st = ""
for i in arr:
    if int(i[1]) % 2 == 0:
        st += (i[0]*int(i[1]))
    else:
        st += (i[0]+i[1])
print(st)
