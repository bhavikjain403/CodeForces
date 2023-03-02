class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        l,r=101,-101
        d,u=101,-101
        for i in range(n):
            x,y=map(int,input().split())
            l=min(l,x)
            d=min(d,y)
            r=max(r,x)
            u=max(u,y)
        if u*d>=0:
            ans=max(abs(u),abs(d))*2
        else:
            ans=2*(u-d)
        if r*l>=0:
            ans+=max(abs(r),abs(l))*2
        else:
            ans+=2*(r-l)
        print(ans)
 
obj=solve()