from math import log2

class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        ans=0
        for i in range(1,n):
            if a[i]<a[i-1]:
                ans=max(ans,int(1+log2(a[i-1]-a[i])))
                a[i]=a[i-1]
        print(ans)
 
obj=solve()