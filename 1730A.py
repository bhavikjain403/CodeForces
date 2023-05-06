from collections import defaultdict

class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,c=map(int, input().split())
        a = list(map(int, input().split()))
        ans=0
        d = defaultdict(int)
        for i in a:
            d[i]+=1
            if d[i]<=c:
                ans+=1
        print(ans)
 
obj=solve()