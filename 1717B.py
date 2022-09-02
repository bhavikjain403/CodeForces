t=int(input())
while t:
    n,k,r,c=map(int,input().split())
    mat=[]
    for i in range(n+1):
        temp=[]
        for j in range(n+1):
            temp.append(".")
        mat.append(temp)
    for x in range(2,n*2+1):
        if abs(r+c-x)%k==0:
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if i+j==x:
                        mat[i][j]="X"
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(mat[i][j],end="",sep="")
        print()
    t-=1