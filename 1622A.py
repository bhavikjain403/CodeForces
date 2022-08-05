t=int(input())
while t:
    a,b,c=map(int,input().split())
    if a==b and c%2==0:
        print("YES")
    elif a==c and b%2==0:
        print("YES")
    elif b==c and a%2==0:
        print("YES")
    elif a==b+c:
        print("YES")
    elif b==a+c:
        print("YES")
    elif c==b+a:
        print("YES")
    else:
        print("NO")
    t-=1