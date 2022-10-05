n=int(input())
h0,m0=map(int,input().split())
c,cash=1,1
for i in range(n-1):
    h,m=map(int,input().split())
    if h==h0 and m==m0:
        c+=1
        cash=max(c,cash)
    else:
        c=1
    h0,m0=h,m
print(cash)