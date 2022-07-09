t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    if n>1:
        a = sorted(l)
        for i in range(n-1):
            if a[i]==l[i]:
                a[i], a[i+1]= a[i+1],a[i]
        if a[n-1]==l[n-1]:
            a[n-2],a[n-1]=a[n-1],a[n-2]
        print(*a)
    else:
        print('-1')
    t-=1