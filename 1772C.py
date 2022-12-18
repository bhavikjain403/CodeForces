class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        k,n=map(int,input().split())
        ans=[]
        l=0
        i=1
        d=1
        s=set()
        while l<k:
            if i<=n:
                ans.append(i)
                s.add(i)
                i+=d
                d+=1
                l+=1
            else:
                break
        for i in range(n,1,-1):
            if l==k:
                break
            if i not in s:
                l+=1
                ans.append(i)
        ans.sort()
        print(*ans)

obj=solve()