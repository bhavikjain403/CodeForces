from turtle import pen


t = int(input())
while t:
    x1,p1=map(int, input().split())
    x2,p2=map(int, input().split())
    m = min(p1,p2)
    p1-=m
    p2-=m
    if p1>6:
        print(">")
    elif p2>6:
        print("<")
    else:
        for i in range(p1):
            x1*=10
        for i in range(p2):
            x2*=10
        if(x1>x2):
            print('>')
        elif x1<x2:
            print('<')
        else:
            print('=')
    t-=1