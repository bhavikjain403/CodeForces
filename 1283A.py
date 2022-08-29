t=int(input())
while t:
    h,m=map(int,input().split())
    print((24-h)*60-m)
    t-=1