class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n = int(input())
        s = input()
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                print(i + 1, i + 2)
                break
        else:
            print(-1, -1)
 
obj=solve()