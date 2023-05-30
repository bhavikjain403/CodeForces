class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        a,b= map(int, input().split())
        print(min(min(a, b), (a+b)//4))
    
obj=solve()