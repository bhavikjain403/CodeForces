class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        s=input()
        i,j=0,n-1
        ans=n
        while i<=j:
            if s[i]!=s[j]:
                ans-=2
            else:
                break
            i+=1
            j-=1
        print(ans)

obj=solve()