t=int(input())
while t:
    a,b,x,y,n=map(int,input().split())
    if n>=(a-x)+(b-y):
        print(x*y)
    else:
        if n>=(a-x):
            t1=(x*(b-(n-(a-x))))
        else:
            t1=((a-n)*b)
        if n>=(b-y):
            t2=(y*(a-(n-(b-y))))
        else:
            t2=((b-n)*a)
        print(min(t1,t2))
    t-=1