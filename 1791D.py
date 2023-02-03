class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        s=input()
        data=[]
        for i in range(n):
            data.append([0]*26)
        for i in range(n):
            if i>0:
                data[i]=data[i-1].copy()
            data[i][ord(s[i])-97]+=1
        ans=0
        d=data[-1].copy()
        for i in range(n-1):
            cpy,c=d.copy(),0
            for j in range(26):
                cpy[j]-=data[i][j]
            for j in range(26):
                if cpy[j]:
                    c+=1
                if data[i][j]:
                    c+=1
            ans=max(ans,c)
        print(ans)

obj=solve()