class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        ans=1
        for i in a:
            ans*=i
        ans+=n-1
        ans*=2022
        print(ans)
 
obj=solve()