class solve:
    def digisum(self,x):
        ans=0
        while x:
            ans+=x%10
            x=x//10
        return ans

    def solution(self):
        n=int(input())
        if n<10:
            print(n)
            return
        ans=0
        while ans*10+9<=n:
            ans=ans*10+9
        print(self.digisum(ans)+self.digisum(n-ans))

obj=solve()
obj.solution()