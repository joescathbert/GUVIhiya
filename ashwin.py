dict1 = {}
dict2 = {}
x=97
res=''
a,b = map(str,input().split())
for i in range(1,27):
  dict1[chr(x)] = i
  x+=1
x=97
for i in range(1,27):
  dict2[i] = chr(x)
  x+=1
for i in range(len(a)):
  t1= dict1.get(a[i])
  t2 =dict1.get(b[i])
  if(t1+t2<27):
    res+=(dict2.get(t1+t2))
  else:
    print(t1+t2)
    t3 = t1+t2%26
print(res)
