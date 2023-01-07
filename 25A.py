class solve:
    def __init__(self):
        n=int(input())
        a=list(map(int,input().split()))
        e,o,i1,i2=0,0,0,0
        for i in range(n):
            if a[i]%2:
                o+=1
                i1=i+1
            else:
                e+=1
                i2=i+1
            if i>=2:
                if o==1:
                    print(i1)
                    break
                elif e==1:
                    print(i2)
                    break
 
obj=solve()