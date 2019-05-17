import math
n = int(input())
if n == 1:
    print(3)
else:
    m = math.floor(math.log2(n+1))
    k = n - sum([2**i for i in range(m)])
    s = ""
    for i in range(1,m+1):
        if k % (2**i) in [x for x in range((2**i)//2)]:
            s += '3'
        else:
            s += '4'
    print(int(s[::-1]))
