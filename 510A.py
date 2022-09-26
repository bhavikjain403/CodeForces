n,m=map(int,input().split())
ans=[]
turn=0
for i in range(n):
    if i%2==0:
        print("#"*m)
    else:
        if turn%2==0:
            print("."*(m-1)+"#")
            turn+=1
        else:
            print("#"+"."*(m-1))
            turn+=1