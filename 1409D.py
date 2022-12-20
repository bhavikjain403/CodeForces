class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def total(self,n):
        ans=0
        while n:
            ans+=n%10
            n//=10
        return ans
    
    def solution(self):
        n,s=map(int,input().split()) 
        if self.total(n)<=s:
            print(0)
            return
        ans=0
        pow=1
        for i in range(18):
            d=(n//pow)%10
            temp = pow*((10-d))
            ans+=temp
            n+=temp
            if self.total(n)<=s:
                print(ans)
                return
            pow*=10
        print(ans)

obj=solve()