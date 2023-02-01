class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,m,d=map(int,input().split())
        p=list(map(int,input().split()))
        a=list(map(int,input().split()))
        idx={}
        for i in range(n):
            idx[p[i]]=i
        ans1=float('inf')
        ans2=float('inf')
        for i in range(m-1):
            j=i+1
            if idx[a[i]]>idx[a[j]]:
                print("0")
                return
            diff=idx[a[j]]-idx[a[i]]
            if diff-1>=d:
                print("0")
                return
            ans1=min(ans1,diff)
            if idx[a[i]]+n-1-idx[a[j]]>=d-diff+1:
                ans2=min(ans2,d-diff+1)
        print(min(ans1,ans2))

obj=solve()