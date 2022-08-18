t=int(input())
while t:
    x=input()
    l=len(x)
    if l==4:
        print((int(x[0])-1)*10+10)
    elif l==3:
        print((int(x[0])-1)*10+6)
    elif l==2:
        print((int(x[0])-1)*10+3)
    else:
        print((int(x[0])-1)*10+1)
    t-=1