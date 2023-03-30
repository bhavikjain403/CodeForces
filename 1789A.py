from math import gcd

class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        for i in range(n-1):
            for j in range(i+1,n):
                if gcd(a[i],a[j])<=2:
                    print("YES")
                    return
        print("NO")
 
obj=solve()