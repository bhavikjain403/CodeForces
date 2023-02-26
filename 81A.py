class solve:
    def __init__(self):
        s=input()
        n=len(s)
        ans=[]
        l=0
        for i in range(n):
            if l==0 or ans[-1]!=s[i]:
                ans.append(s[i])
                l+=1
            else:
                ans.pop()
                l-=1
        print("".join(ans))

obj=solve()