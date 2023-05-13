class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n, m = map(int, input().split())
        print(n + m - 3 + min(n, m) + min(max(n, m) - 1, 1))
 
obj=solve()