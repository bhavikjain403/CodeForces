from statistics import mode

class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        d=dict()
        for i in range(n-1):
            d[i]=[]
        for i in range(n):
            a=list(map(int,input().split()))
            for j in range(n-1):
                d[j].append(a[j])
        ans=[0]*n
        c=0
        v=set()
        for i in d:
            temp={}
            n1,n2=0,0
            for j in d[i]:
                if temp.get(j,0)==0:
                    temp[j]=1
                    if n1==0:
                        n1=j
                    elif n2==0:
                        n2=j
                else:
                    temp[j]+=1
            if temp[n1]>temp[n2]:
                maxi=n1
                mini=n2
            else:
                maxi=n2
                mini=n1
            if maxi not in v:
                v.add(maxi)
                ans[c]=maxi
                c+=1
            if mini not in v:
                v.add(mini)
                ans[c]=mini
                c+=1
            if c>=n:
                break
        print(*ans)
 
obj=solve()