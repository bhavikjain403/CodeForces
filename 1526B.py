class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
            
    def solution(self):
        n=int(input())
        if n>=111*(n%11):
            print("YES")
        else:
            print("NO")

obj=solve()