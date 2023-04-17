class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,k=map(int, input().split())
        a=list(map(int, input().split()))
        if sum(a)>0:
            print("YES")
        else:
            print("NO")
 
obj=solve()