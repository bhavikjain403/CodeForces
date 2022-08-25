t=int(input())
while t:
    a,b=map(int,input().split())
    if a%b==0:
        print("0")
    else:
        print(b*(a//b+1)-a)
    t-=1