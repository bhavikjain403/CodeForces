class solve:
    def __init__(self):
        def check(x):
            s = str(x)
            cnt = 0
            for c in s:
                if c != '0':
                    cnt += 1
            return cnt == 1
        self.a = []
        for i in range(1, 1000000):
            if check(i):
                self.a.append(i)
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        ans=0
        for x in self.a:
            if x <= n:
                ans += 1
        print(ans)
 
obj=solve()