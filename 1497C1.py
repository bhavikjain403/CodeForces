class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,k=map(int,input().split())
        if n%2:
            print(n//2,n//2,1)
        elif n%4:
            print(n//2-1,n//2-1,2)
        else:
            print(n//2,n//4,n//4)
 
obj=solve()