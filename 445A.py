class solve:
    def __init__(self):
        n,m=map(int,input().split())
        for i in range(n):
            s=list(input())
            for j in range(m):
                if s[j]==".":
                    if (i+j)%2:
                        s[j]="W"
                    else:
                        s[j]="B"
            print("".join(s))
 
obj=solve()