class solve:
    def __init__(self):
        n=int(input())
        a=list(map(int,input().split()))
        if n==1:
            print("0 1")
        if n==2:
            print("1 1")
        else:
            c1,c2=0,0
            i,j=0,n-1
            s1,s2=a[i],a[j]
            while i<=j:
                if s1>s2:
                    j-=1
                    s2+=a[j]
                    c2+=1
                else:
                    i+=1
                    s1+=a[i]
                    c1+=1
            print(c1,c2)
 
obj=solve()