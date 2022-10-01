n,d=map(int,input().split())
l=list(map(int,input().split()))
s=sum(l)+10*(n-1)
if s>d:
    print(-1)
else:
    print(2*(n-1)+(d-s)//5)