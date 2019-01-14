def newfunc(s, a):
    if len(s) == 1 or (len(s) == 2 and int(s) < 27):
        a += 1
        return a
    else:
        for i in range(1,3):
            if int(s[:i]) < 27:
                a = newfunc(s[i:], a)
            else:
                return a
        return a

print(newfunc(input(),0))
