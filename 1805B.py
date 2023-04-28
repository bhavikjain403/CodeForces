class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n = int(input())
        s = input()
        ind = s.rfind(min(s))
        print(s[ind] + s[:ind] + s[ind + 1:])
 
obj=solve()