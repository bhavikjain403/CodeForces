t=int(input())
while t:
    flag=1
    n,k=map(int,input().split())
    data=[0]
    for i in range(1,n+1):
        data.append(i)
    i=1
    while i<=n:
        if(((data[i]+k)*data[i+1])%4==0):
            i+=2
            continue
        else:
            data[i],data[i+1]=data[i+1],data[i]
            if ((data[i]+k)*data[i+1])%4==0:
                i+=2
                continue
            else:
                print("NO")
                flag=0
                break
    if flag:
        print("YES")
        i=1
        while i<=n:
            print(f"{data[i]} {data[i+1]}")
            i+=2
    t-=1