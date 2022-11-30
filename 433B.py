class solve:
    def __init__(self):
        n=int(input())
        a=list(map(int,input().split()))
        m=int(input())
        if n==1:
            for i in range(m):
                typ,l,r=map(int,input().split())
                print(a[0])
        else:
            data=[a[0]]
            b=sorted(a)
            data2=[b[0]]
            for i in range(1,n):
                data.append(data[i-1]+a[i])
                data2.append(data2[i-1]+b[i])
            for i in range(m):
                typ,l,r=map(int,input().split())
                if l==1:
                    if typ==1:
                        print(data[r-1])
                    else:
                        print(data2[r-1])
                else:
                    if typ==1:
                        print(data[r-1]-data[l-2])
                    else:
                        print(data2[r-1]-data2[l-2])

obj=solve()