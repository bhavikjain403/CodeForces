class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,m=map(int,input().split())
        p=list(map(int,input().split()))
        ans=[-1]*n
        t=0
        s=set()
        for i in p:
            t+=1
            if n==0:
                break
            if i not in s:
                ans[n-1]=t
                n-=1
                s.add(i)
        print(*ans)
 
obj=solve()