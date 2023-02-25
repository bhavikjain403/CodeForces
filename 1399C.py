from collections import Counter

class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        c=Counter(a)
        ans=0
        for i in range(2,2*n+1):
            temp=0
            for j in range(1,(i+1)//2):
                if i-j<=n:
                    temp+=min(c[j],c[i-j])
            if i%2==0:
                temp+=c[i//2]//2
            ans=max(ans,temp)
        print(ans)

obj=solve()