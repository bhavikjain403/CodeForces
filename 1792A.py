class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        c=0
        for i in a:
            c+=(i==1)
        print(n-c//2)

obj=solve()