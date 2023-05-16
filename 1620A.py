class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        s=input()
        if s.count("N")==1:
            print("NO")
        else:
            print("YES")
 
obj=solve()