class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n=int(input())
        s=input()
        ans,i="",0
        while i<n and s[i]=="0":
            ans+=s[i]
            i+=1
        x=i
        while i<n:
            if s[i]=="0":
                x=i
            i+=1
        ans+=s[x:n]
        print(ans)
obj=solve()