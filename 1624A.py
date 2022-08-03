t=int(input())
while t:
    n=int(input())
    l=list(map(int,input().split()))
    print(max(l)-min(l))
    t-=1