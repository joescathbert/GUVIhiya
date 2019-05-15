def recur(tempbrack, rembrackets, stability, bracketscount, tempresultopt,tempbrackopt,b):
    if len(tempbrack) == bracketscount:
        if stability == 0 and tempbrack not in tempresultopt:
            tempresultopt.append(tempbrack)
            print("".join(tempbrack))
        return tempresultopt, tempbrackopt
    else:
        for i in range(len(rembrackets)):
            if rembrackets[i] == '{': stab = stability + 1
            else: stab = stability - 1
            #print(stability)
            if stab >= 0:
                rembracketd = rembrackets.copy()
                rembracketd.remove(rembrackets[i])
                #print(stability,tempbrack+[rembrackets[i]],rembracketd,b)
                if [tempbrack, rembrackets, stability] not in tempbrackopt: 
                    tempresultopt, tempbrackopt = recur(tempbrack + [rembrackets[i]], rembracketd, stab, bracketscount, tempresultopt, tempbrackopt, b+1)
        tempbrackopt.append([tempbrack, rembrackets, stability])
        return tempresultopt, tempbrackopt

n = int(input())
arr = ['{' if x % 2 == 0 else '}' for x in range(n*2)]
a, c = recur([], arr, 0, n*2, [], [], 0)
