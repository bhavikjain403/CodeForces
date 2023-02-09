class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        prod=1
        for i in a:
            prod*=i
        left=1
        for i in range(n-1):
            left*=a[i]
            prod//=a[i]
            if left==prod:
                print(i+1)
                return
        print("-1")

obj=solve()