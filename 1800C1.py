import heapq

class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        data=[]
        l=0
        heapq.heapify(data)
        ans=0
        for i in a:
            if i==0:
                if l==0:
                    continue
                else:
                    l-=1
                    ans-=heapq.heappop(data)
            else:
                heapq.heappush(data,-1*i)
                l+=1
        print(ans)
 
obj=solve()