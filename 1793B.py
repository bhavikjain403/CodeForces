class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        a,b=map(int,input().split())
        n=2*(a-b)
        print(n)
        ans=[0]*n
        idx=0
        for i in range(b,a+1):
            ans[idx]=i
            idx+=1
        for i in range(a-1,b,-1):
            ans[idx]=i
            idx+=1
        print(*ans)
 
obj=solve()