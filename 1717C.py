class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
            
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        for i in range(n):
            if b[i]>=a[i] and (b[i]==a[i] or b[i]<=b[(i+1)%n]+1):
                continue
            else:
                print("NO")
                return
        print("YES")

obj=solve()