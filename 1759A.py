class solve:
    def __init__(self):
        self.s="Yes"*18
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        if self.s.find(input())>=0:
            print("YES")
        else:
            print("NO")
 
obj=solve()