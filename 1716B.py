class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n = int(input())
        p = [i + 1 for i in range(n)]
        print(n)
        for i in range(n):
            print(*p)
            if i < n - 1:
                p[i], p[i + 1] = p[i + 1], p[i]
 
obj=solve()