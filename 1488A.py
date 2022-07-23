from math import log10

t=int(input())
while t:
    x,y=map(int,input().split())
    c=0
    k=0
    while k<y:
        if k+x>y:
            c+=y-k
            break
        p=int(log10((y-k)/x))
        k+=x*10**p
        c+=1
    print(c)
    t-=1