class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n, k = map(int, input().split())
        p = list(map(int, input().split()))
        for i in range(0, n):
            p[i] -= 1

        bad = 0
        for i in range(0, n):
            if p[i] % k != i % k:
                bad += 1

        if bad == 0:
            print(0)
        elif bad == 2:
            print(1)
        else:
            print(-1)
 
obj=solve()