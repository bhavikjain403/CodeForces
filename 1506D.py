from collections import Counter
import heapq

class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
            
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        c=Counter(a).values()
        l=len(c)
        q=[]
        for i in c:
            heapq.heappush(q,-1*i)
        ans=n
        while l>1:
            temp1=heapq.heappop(q)*-1
            temp2=heapq.heappop(q)*-1
            l-=2
            ans-=2
            temp1-=1
            temp2-=1
            if temp1:
                heapq.heappush(q,temp1*-1)
                l+=1
            if temp2:
                heapq.heappush(q,temp2*-1)
                l+=1
        print(ans)

obj=solve()