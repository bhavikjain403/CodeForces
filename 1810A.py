class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        for i in range(n):
            if a[i]<=i+1:
                print("YES")
                return
        print("NO")
 
obj=solve()