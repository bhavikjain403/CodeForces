t=int(input())
while t:
    x=int(input())
    if x<=3:
        print(x-1)
    elif x%2==0:
        print(2)
    else:
        print(3)
    t-=1