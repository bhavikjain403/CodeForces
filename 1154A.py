x,y,z,w=map(int,input().split())
m=max(x,y,z,w)
if w==m:
    print(x+y-w,x+z-w,y+z-w)
elif x==m:
    print(w+y-x,w+z-x,y+z-x)
elif y==m:
    print(x+w-y,x+z-y,w+z-y)
else:
    print(x+y-z,x+w-z,y+w-z)