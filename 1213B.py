class solve:
    def solution(self):
        for i in range(int(input())):
            n=int(input())
            a=list(map(int,input().split()))
            ans,mini=0,a[n-1]
            if n>1:
                for j in range(n-2,-1,-1):
                    if a[j]>mini:
                        ans+=1
                    else:
                        mini=a[j]
            print(ans)
obj=solve()
obj.solution()