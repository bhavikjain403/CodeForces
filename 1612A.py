class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        x, y = map(int, input().split())
        xc = -1
        yc = -1
        for j in range(0, 51):
            for k in range(0, 51):
                if 2 * (j + k) == x + y and 2 * (abs(x - j) + abs(y - k)) == x + y:
                    xc, yc = j, k
        print(xc, yc)
 
obj=solve()