class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        if n%2:
            print(-1)
        else:
            print(1,n//2)

obj=solve()