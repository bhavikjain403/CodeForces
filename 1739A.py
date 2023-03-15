class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,m=map(int,input().split())
        print(n//2+1,m//2+1)
 
obj=solve()