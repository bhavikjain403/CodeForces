class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        x, k = map(int, input().split())
        if x % k != 0:
            print(1)
            print(x)
        else:
            print(2)
            print(1, x - 1)
    
obj=solve()