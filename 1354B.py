class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
            
    def solution(self):
        s=input()
        if len(set(s))==3:
            l=len(s)
            ans=float('inf')
            i,j,k=0,0,0
            s1=set()
            for p in range(l):
                if s[p]=="1":
                    i=p
                if s[p]=="2":
                    j=p
                if s[p]=="3":
                    k=p
                s1.add(s[p])
                if len(s1)==3:
                    ans=min(ans,max(i,j,k)-min(i,j,k))
            print(ans+1)
            return
        print("0")

obj=solve()