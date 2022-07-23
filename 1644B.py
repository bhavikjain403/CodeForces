t=int(input())
while t:
    n=int(input())
    a=[]
    for i in range(n,0,-1):
        a.append(i)
    print(*a)
    for i in range(n-1):
        a[i],a[i+1]=a[i+1],a[i]
        print(*a)
        a[i],a[i+1]=a[i+1],a[i]
    t-=1