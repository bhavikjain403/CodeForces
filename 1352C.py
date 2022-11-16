class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n,k=map(int,input().split())
        if k<n:
            print(k)
            return
        q=k//(n-1)
        p=q*(n-1)+q
        if k%(n-1):
            print(p+k%(n-1))
        else:
            if p%n:
                print(p)
            else:
                print(p-1)

obj=solve()