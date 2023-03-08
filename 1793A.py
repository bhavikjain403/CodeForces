class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        a,b=map(int,input().split())
        n,m=map(int,input().split())
        q=n//(m+1)
        r=n-q*(m+1)
        print(q*min(a*m,b*(m+1))+r*min(a,b))
 
obj=solve()