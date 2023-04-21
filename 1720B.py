class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        a.sort()
        print(a[n-1]+a[n-2]-a[0]-a[1])
 
obj=solve()