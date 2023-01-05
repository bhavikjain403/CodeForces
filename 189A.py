class solve:
    def __init__(self):
        n,a,b,c=map(int,input().split())
        ans=0
        i=0
        while i*a<=n:
            j=0
            while i*a+j*b<=n:
                left=n-i*a-j*b
                if left%c==0:
                    ans=max(ans,i+j+left//c)
                j+=1
            i+=1
        print(ans)
 
obj=solve()