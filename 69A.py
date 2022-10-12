n=int(input())
x,y,z=0,0,0
while n:
    a,b,c=map(int,input().split())
    x+=a
    y+=b
    z+=c
    n-=1
if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")