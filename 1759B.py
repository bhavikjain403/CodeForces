class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        s += sum(a)
        sm = 0
        cnt = 0
        for i in range(1, s + 1):
            if sm >= s:
                break
            sm += i
            cnt = i
        if sm != s or max(a) > cnt or cnt <= n:
            print("NO")
        else:
            print("YES")
 
obj=solve()