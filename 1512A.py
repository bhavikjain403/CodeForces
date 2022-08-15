t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    if a[0]!=a[1]:
        if a[0]==a[2]:
            print("2")
        else:
            print("1")
    else:
        for i in range(n-1):
            if a[i]!=a[i+1]:
                print(i+2)
                break
    t-=1