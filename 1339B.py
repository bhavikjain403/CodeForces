class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        ans=[0]*n
        a.sort()
        start,end=0,n-1
        idx=n-1
        c=0
        while end>=start:
            if c%2:
                ans[idx]=a[start]
                start+=1
                c=0
            else:
                ans[idx]=a[end]
                end-=1
                c=1
            idx-=1
        print(*ans)

obj=solve()