class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        s=input()
        f=-1
        for i in range(n//2+1):
            if s[i]!=s[n-i-1]:
                f=i
                break
        if f==-1:
            print("YES")
        else:
            g=f
            for i in range(f,n//2+1):
                if s[i]==s[n-i-1]:
                    g=i
                    break
            if g==f:
                print("YES")
                return
            for i in range(g,n//2+1):
                if s[i]!=s[n-i-1]:
                    print("NO")
                    return
            print("YES")
 
obj=solve()