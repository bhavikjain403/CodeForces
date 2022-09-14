n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
x.pop(0)
y.pop(0)
x,y=set(x),set(y)
flag=1
for i in range(1,n+1):
    if i in x or i in y:
        continue
    else:
        flag=0
        break
if flag:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")