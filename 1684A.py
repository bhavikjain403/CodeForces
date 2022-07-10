def split(n):
    mini = n%10
    n=n//10
    while n:
        t=n%10
        if mini>t:
            mini=t
        n=n//10
    return mini

t = int(input())
while t:
    n = int(input())
    if n//10==0:
        print(n)
    elif (n//10)//10==0:
        print(n%10)
    else:
        print(split(n))
    t-=1