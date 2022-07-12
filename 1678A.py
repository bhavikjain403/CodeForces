t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    z = a.count(0)
    if(z):
        print(n-z)
    else:
        s = len(set(a))
        if n==s:
            print(n+1)
        else:
            print(n)
    t-=1