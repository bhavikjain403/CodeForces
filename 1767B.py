class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n = int(input())
        a = list(map(int, input().split()))
        x = a[0]
        a = sorted(a[1:])
        for i in a:
            if i > x:
                x += (i - x + 1) // 2
        print(x)
 
obj=solve()