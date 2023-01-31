class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        if max(a[1:n-1])==1 or (n==3 and a[1]%2):
            print("-1")
            return
        ans=0
        for i in range(1,n-1):
            ans+=(a[i]+1)//2
        print(ans)

obj=solve()