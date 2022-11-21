class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        ans=[]
        b=sorted(a)
        m=b[n-1]
        if b[n-1]!=b[n-2]:
            m2=b[n-2]
            for i in a:
                if i==m:
                    ans.append(i-m2)
                else:
                    ans.append(i-m)
        else:
            for i in a:
                ans.append(i-m)
        print(*ans)

obj=solve()