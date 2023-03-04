class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        if n==1:
            print(a[0])
            return
        for i in range(n):
            if a[i]==1:
                a[i]+=1
        for i in range(1,n):
            if a[i]%a[i-1]==0:
                a[i]+=1
        print(*a)
 
obj=solve()