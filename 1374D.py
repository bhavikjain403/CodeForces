class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n,k=map(int,input().split())
        a=list(map(int,input().split()))
        d={}
        ans=0
        for i in a:
            if i%k:
                temp=k-i%k
                if temp not in d:
                    d[temp]=1
                else:
                    d[temp]+=1
        flag=0
        for i in d:
            flag=1
            ans=max(ans,k*(d[i]-1)+i)
        if flag:
            ans+=1
        print(ans)
 
obj=solve()