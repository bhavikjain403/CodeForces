class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
    
    def calSum(self,n):
        arr=[]
        l=0
        while n:
            arr.append(n%10)
            l+=1
            n//=10
        return arr

    def solution(self):
        n=int(input())
        if n%2:
            x,y=(n+1)//2,(n-1)//2
            if x%10==0 and y%10==9:
                arr=self.calSum(n)
                f=0
                x,y=0,0
                p=1
                for i in arr:
                    if i%2:
                        x+=(i//2+f)*p
                        y+=(i//2-f+1)*p
                        f=1-f
                    else:
                        x,y=x+(i//2)*p,y+(i//2)*p
                    p*=10
        else:
            x,y=n//2,n//2
        print(x,y)

obj=solve()