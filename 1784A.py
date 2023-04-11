class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        a.sort()
        ans=0
        for i in range(n):
            if i:
                prev=a[i-1]
            else:
                prev=0
            if a[i]>prev+1:
                ans+=a[i]-prev+1
                a[i]=prev+1
        print(ans)
 
obj=solve()