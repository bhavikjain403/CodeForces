class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n, k = map(int, input().split())
        s = input()
        if s == s[::-1] or k == 0:
            print(1)
        else:
            print(2)
 
obj=solve()