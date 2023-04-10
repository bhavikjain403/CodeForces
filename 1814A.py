class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n, k = map(int, input().split())
        for x in range(2):
            if n - x * k >= 0 and (n - x * k) % 2 == 0:
                print("YES")
                return
        print("NO")
 
obj=solve()