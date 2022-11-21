class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        a=list(map(int,input().split()))
        a.sort()
        print(a[1])

obj=solve()