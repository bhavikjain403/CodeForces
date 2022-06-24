t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    a = []
    ll=n
    la=0
    i=0
    for i in range(n):
        if l[i] not in a:
            a.append(l[i])
            la+=1
            ll-=1
    if ll%2==0:
        print(la)
    else:
        print(la-1)
    t-=1