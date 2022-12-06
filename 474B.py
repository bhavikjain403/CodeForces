class solve:
    def __init__(self):
        n=int(input())
        a=list(map(int,input().split()))
        m=int(input())
        m=list(map(int,input().split()))
        data={}
        i,j=1,0
        s=sum(a)
        p=a[0]
        while i<=s:
            while i<=p:
                data[i]=j+1
                i+=1
            j+=1
            if j<n:
                p+=a[j]
        for i in m:
            print(data[i])

obj=solve()