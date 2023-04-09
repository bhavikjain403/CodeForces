class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        s=input()
        for i in range(n-1):
            for j in range(i+1,n):
                if a[i]==a[j]:
                    if s[i]!=s[j]:
                        print("NO")
                        return
        print("YES")
 
obj=solve()