class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        a,b,c=map(int,input().split())
        print("+" if a+b==c else "-")
 
obj=solve()