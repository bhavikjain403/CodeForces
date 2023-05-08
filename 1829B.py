class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        ans,cnt=0,0
        for i in a:
            if i==0:
                cnt+=1
            else:
                ans=max(ans,cnt)
                cnt=0
        print(max(ans,cnt))
 
obj=solve()