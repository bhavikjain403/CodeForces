class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        if a[0]<b[0]:
            print(0)
            return
        idx={}
        for i in range(n):
            idx[a[i]]=i
            idx[b[i]]=i
        data,mini={},float('inf')
        for i in range(1,2*n,2):
            mini=min(mini,idx[i])
            data[i]=mini
        ans=float('inf')
        for i in range(2,2*n+1,2):
            ans=min(ans,idx[i]+data[i-1])
        print(ans)
 
obj=solve()