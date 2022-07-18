t=int(input())
while t:
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    s=["B"]*m
    for i in a:
        if i-1<=m-i:
            if s[i-1]=="B":
                s[i-1]="A"
            else:
                s[m-i]="A"
        else:
            if s[m-i]=="B":
                s[m-i]="A"
            else:
                s[i-1]="A"
    print(*s,sep="")
    t-=1