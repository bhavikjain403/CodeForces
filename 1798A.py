class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        for i in range(n):
            if a[i] > b[i]:
                a[i], b[i] = b[i], a[i]
        if a[-1] == max(a) and b[-1] == max(b):
            print("YES")
        else:
            print("NO")
 
obj=solve()