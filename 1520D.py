from collections import defaultdict

class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        d=defaultdict(int)
        for i in range(n):
            d[a[i]-i-1]+=1
        ans=0
        for i in d:
            ans+=d[i]*(d[i]-1)//2
        print(ans)
obj=solve()