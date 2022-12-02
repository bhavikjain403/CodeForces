class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
            
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        a.sort()
        m=float('inf')
        i1,i2,p=-1,-1,-1
        for i in range(1,n):
            if m>a[i]-a[i-1]:
                m=a[i]-a[i-1]
                i1=a[i-1]
                i2=a[i]
                p=i
        ans=[i1]
        for i in range(p+1,n):
            ans.append(a[i])
        for i in range(p-1):
            ans.append(a[i])
        ans.append(i2)
        print(*ans)

obj=solve()