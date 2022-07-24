t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        if a[i]!=i+1:
            break
    j=a.index(i+1)
    b=a[i:j+1]
    a=a[:i]+b[::-1]+a[j+1:]
    print(*a)
    t-=1