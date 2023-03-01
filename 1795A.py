class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,m=map(int,input().split())
        a=input()
        b=input()
        a=a+b[::-1]
        ans=0
        for i in range(1,n+m):
            ans+=a[i]==a[i-1]
        if ans<=1:
            print("YES")
        else:
            print("NO")
 
obj=solve()