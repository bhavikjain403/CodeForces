def col(a,c,n):
    flag=0
    for i in range(n):
        if a[i][c-1]=="B":
            flag=1
            break
    return flag

t=int(input())
while t:
    n,m,r,c=map(int,input().split())
    a=[]
    flag=0
    for i in range(n):
        s=input()
        a.append(s)
        if "B" in s:
            flag=1
    if flag==0:
        print("-1")
    else:
        if a[r-1][c-1]=="B":
            print("0")
        elif "B" in a[r-1]:
            print("1")
        elif col(a,c,n):
            print("1")
        else:
            print("2")
    t-=1