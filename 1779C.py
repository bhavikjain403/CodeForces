import heapq

class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,m=map(int,input().split())
        a=list(map(int,input().split()))
        ans=[]
        heapq.heapify(ans)
        presum,c=0,0
        for i in range(m,n):
            presum+=a[i]
            if a[i]<0:
                heapq.heappush(ans,a[i])
            while presum<0:
                c+=1
                temp=heapq.heappop(ans)
                presum-=2*temp
        if a[m-1]<=0:
            presum=a[m-1]
        elif m!=1:
            c+=1
            presum=a[m-1]*-1
        ans=[]
        heapq.heapify(ans)
        for i in range(m-2,0,-1):
            presum+=a[i]
            if a[i]>0:
                heapq.heappush(ans,-1*a[i])
            while presum>0:
                c+=1
                temp=-1*heapq.heappop(ans)
                presum-=2*temp
        print(c)
 
obj=solve()