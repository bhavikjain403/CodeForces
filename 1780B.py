from math import gcd

class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        data=[0]*n
        data[0]=a[0]
        for i in range(1,n):
            data[i]=data[i-1]+a[i]
        ans=1
        for i in range(n-1):
            ans=max(ans,gcd(data[i],data[n-1]-data[i]))
        print(ans)
 
obj=solve()