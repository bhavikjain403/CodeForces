class solve:
    def __init__(self):
        s=input()
        n=len(s)
        ans=0
        for i in range(n-2):
            if s[i]=="Q":
                for j in range(i+1,n-1):
                    if s[j]=="A":
                        for k in range(j+1,n):
                            if s[k]=="Q":
                                ans+=1
        print(ans)
 
obj=solve()