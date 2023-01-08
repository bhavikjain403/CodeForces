class solve:
    def __init__(self):
        n=int(input())
        a=list(map(int,input().split()))
        c,l,ans=1,0,[]
        for i in range(n):
            if a[i]==c:
                ans.append(2001+i)
                l+=1
                c+=1
        if l==0:
            print(0)
        else:
            print(l)
            print(*ans)
 
obj=solve()