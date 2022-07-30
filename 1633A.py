t=int(input())
while t:
    n=int(input())
    if n%7==0:
        print(n)
    else:
        d=n%10
        n-=d
        for i in range(0,10):
            if (n+i)%7==0:
                print(n+i)
                break
    t-=1