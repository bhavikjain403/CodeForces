class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        if a[0]==a[n - 1]:
            print('NO')
        else:
            print('YES')
            print(a[n - 1], end = ' ')
            print(*(a[0:n-1]))
 
obj=solve()