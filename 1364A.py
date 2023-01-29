class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,x=map(int,input().split())
        a=list(map(int,input().split()))
        suffix=sum(a)
        prefix=suffix
        ans1=n
        if suffix%x:
            print(ans1)
            return
        flag1=0
        for i in range(n-1,-1,-1):
            suffix-=a[i]
            ans1-=1
            if suffix%x:
                flag1=1
                break
        ans2=n
        flag2=0
        for i in range(n):
            prefix-=a[i]
            ans2-=1
            if prefix%x:
                flag2=1
                break
        if flag1==0 and flag2==0:
            print(-1)
        else:
            print(max(ans1,ans2))

obj=solve()