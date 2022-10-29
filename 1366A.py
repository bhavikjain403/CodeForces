t=int(input())
while t:
    a,b=map(int,input().split())
    maxi,mini=max(a,b),min(a,b)
    if mini*2<=maxi:
        print(mini)
    else:
        print((a+b)//3)
    t-=1