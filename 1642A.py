t=int(input())
while t:
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    x3,y3=map(int,input().split())
    if y1==y2:
        if y3<y1:
            print(abs(x1-x2))
        else:
            print("0")
    elif y1==y3:
        if y2<y1:
            print(abs(x1-x3))
        else:
            print("0")
    elif y3==y2:
        if y1<y2:
            print(abs(x3-x2))
        else:
            print("0")
    else:
        print("0")
    t-=1