t=int(input())
while t:
    a,b=map(int,input().split())
    d=abs(a-b)
    if d%10:
        print(d//10+1)
    else:
        print(d//10)
    t-=1