class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        input()
        xs = []
        ys = []
        for j in range(3):
            x, y = map(int, input().split())
            xs.append(x)
            ys.append(y)
        print('YES' if len(set(xs)) == 3 or len(set(ys)) == 3 else 'NO')
 
obj=solve()