t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    if a==sorted(a):
        print("0")
    elif a[0]==1 or a[-1]==n:
        print("1")
    elif a[0]==n and a[-1]==1:
        print("3")
    else:
        print("2")
    t-=1