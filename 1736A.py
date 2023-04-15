class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        total=sum(a)-sum(b)
        ans=0
        for i in range(n):
            ans+=a[i]^b[i]
        print(min(ans,abs(total)+1))
 
obj=solve()