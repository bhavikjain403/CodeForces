t=int(input())
while t:
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    data=[]
    for i in range(n):
        data.append([a[i],b[i]])
    data.sort(key=lambda x:x[0])
    for i in range(n):
        if data[i][0]<=k:
            k+=data[i][1]
        else:
            break
    print(k)
    t-=1