n,m,a=map(int,input().split())
x,y=n//a,m//a
if n%a:
    x+=1
if m%a:
    y+=1
print(x*y)