class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,k=map(int,input().split())
        k-=1
        print((k+(n%2)*k//(n//2))%n+1)
 
obj=solve()