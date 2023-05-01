class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n, k = map(int, input().split())
        x = -1
        for i in range(0, n + 1):
            if i * (i - 1) / 2 + (n - i) * (n - i - 1) / 2 == k:
                x = i
        if x == -1:
            print("NO")
        else:
            print("YES")
            for i in range(0, n):
                if i < x:
                    print("1 ", end = '')
                else:
                    print("-1 ", end = '')
            print("")
 
obj=solve()