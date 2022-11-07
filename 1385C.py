class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        if n<3:
            print("0")
            return
        i=n-1
        while i>0 and a[i-1]>=a[i]:
            i-=1
        j=i
        while j>0 and a[j-1]<=a[j]:
            j-=1
        print(j)

obj=solve()