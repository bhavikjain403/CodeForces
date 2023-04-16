class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n, m = map(int, input().split())
        for _ in range(m):
            input()
        print("NO" if n == m else "YES")
 
obj=solve()