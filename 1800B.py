from collections import Counter

class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,k=map(int,input().split())
        s=input()
        c=Counter(s)
        ans=0
        for i in c:
            if i.isupper() and c[i]!=0:
                temp=min(c[i],c.get(i.lower(),0))
                ans+=temp
                c[i]-=temp
                if c.get(i.lower(),0):
                    c[i.lower()]-=temp
                # if k:
                #     if c[i]!=c[i.lower()]:
                #         add=max(c[i],c[i.lower()])//2
                #         if add>k:
                #             ans+=k
                #             k=0
                #         else:
                #             ans+=add
                #             k-=add
            elif i.islower() and c[i]!=0:
                temp=min(c[i],c.get(i.upper(),0))
                ans+=temp
                c[i]-=temp
                if c.get(i.upper(),0):
                    c[i.upper()]-=temp
                # if k:
                #     if c[i]!=c[i.upper()]:
                #         add=max(c[i],c[i.upper()])//2
                #         if add>k:
                #             ans+=k
                #             k=0
                #         else:
                #             ans+=add
                #             k-=add
        if k:
            for i in c:
                add=c[i]//2
                ans+=min(add,k)
                k-=min(add,k)
                if k==0:
                    break
        print(ans)
 
obj=solve()