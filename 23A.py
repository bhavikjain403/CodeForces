from collections import *

class solve:
    def __init__(self):
        s=input()
        n=len(s)
        ans=[s[i: j] for i in range(n) for j in range(i+1, n+1)]
        l=0
        c=Counter(ans)
        for i in c:
            if c[i]>1:
                l=max(l,len(i))
        print(l)
 
obj=solve()