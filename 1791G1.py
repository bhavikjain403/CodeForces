class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,c=map(int,input().split())
        a=list(map(int,input().split()))
        for i in range(n):
            a[i]+=i+1
        a.sort()
        for i in range(n):
            if c<a[i]:
                print(i)
                return
            c-=a[i]
        print(i+1)

obj=solve()