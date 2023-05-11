class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        a.sort()
        ans=float('inf')
        for i in range(2,n):
            ans=min(ans,a[i]-a[i-2])
        print(ans)
 
obj=solve()