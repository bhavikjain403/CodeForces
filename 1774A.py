class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        s=input()
        ans=""
        u=0
        for i in range(n):
            f=(s[i]=="1") and u
            u^=int(s[i])
            if(i!=0):
                if f:
                    ans+="-"
                else:
                    ans+="+"
        print(ans)
 
obj=solve()