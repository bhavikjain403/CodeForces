class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n=int(input())
        i=2
        while i*i<=n and n%i>0:
            i+=1
        if i*i>n:
            print(1,n-1)
        else:
            print(n//i, n-n//i)

obj=solve()