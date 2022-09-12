t=int(input())
while t:
    a,b,c=map(int,input().split())
    t1=abs(a-1)
    t2=abs(b-c)+abs(c-1)
    if t1<t2:
        print("1")
    elif t1>t2:
        print("2")
    else:
        print("3")
    t-=1