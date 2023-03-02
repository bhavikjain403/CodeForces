class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        s=input()
        i,j=1,2
        a,b=s[0],s[1]
        ans=1
        for t in range(1,n-1):
            if (s[i]!=a or s[j]!=b) and s[j]!=a:
                ans+=1
            a,b=s[i],s[j]
            i+=1
            j+=1
        print(ans)
 
obj=solve()