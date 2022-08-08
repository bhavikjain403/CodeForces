t=int(input())
while t:
    a,b,c=map(int,input().split())
    print(max(0,max(b,c)+1-a),max(0,max(a,c)+1-b),max(0,max(a,b)+1-c))
    t-=1