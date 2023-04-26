class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        print(max(a[0] * a[1], a[-1] * a[-2]))
 
obj=solve()