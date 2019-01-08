vow = ['a','e','i','o','u']
n = int(input())
st = list(input())
print("".join([st[i] for i in range(len(st)) if st[i].lower() not in vow][::-1]))
