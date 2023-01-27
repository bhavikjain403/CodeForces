class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,s,r=map(int,input().split())
        ans=[0]*n
        ans[0]=s-r
        rem=r//(n-1)
        left=r%(n-1)
        for i in range(1,n):
            ans[i]=rem
            if left>0:
                ans[i]+=1
                left-=1
        print(*ans)
 
obj=solve()