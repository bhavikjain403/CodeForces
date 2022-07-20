t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    m1=max(a)
    a[a.index(m1)]=0
    print(m1+max(a))
    t-=1