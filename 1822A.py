class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,t=map(int,input().split())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        c=0
        ans=-2
        e=0
        for i in range(n):
            if a[i]+c<=t:
                if b[i]>e:
                    e=b[i]
                    ans=i
            c+=1
        print(ans+1)
 
obj=solve()