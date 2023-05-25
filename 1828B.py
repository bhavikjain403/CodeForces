from math import gcd

class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        ans=0
        a=list(map(int,input().split()))
        for i in range(n):
            ans=gcd(ans,abs(a[i]-i-1))
        print(ans)
    
obj=solve()