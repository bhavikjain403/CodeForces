class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n = int(input())
        s = input()
        cnt = set()
        for i in range(1, n):
            cnt.add(s[i - 1] + s[i])
        print(len(cnt))
 
obj=solve()