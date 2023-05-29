class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n, k = map(int, input().split())
        a = sorted(list(map(int, input().split())))
        ans = 0
        pr = [0] * (n + 1)
        for i in range(n):
            pr[i + 1] = pr[i] + a[i]
        for i in range(k + 1):
            ans = max(ans, pr[n - (k - i)] - pr[2 * i])
        print(ans)
    
obj=solve()