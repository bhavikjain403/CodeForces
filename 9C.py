class solve:
    def __init__(self):
        n=int(input())
        ans=0
        for i in range(1,2**10-1):
            b=int(bin(i).replace("0b",'0'))
            if b<=n:
                ans+=1
            else:
                break
        print(ans)

obj=solve()