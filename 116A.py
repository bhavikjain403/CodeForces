n=int(input())
ans=0
cap=0
for i in range(n):
    a,b=map(int,input().split())
    cap+=b-a
    if cap>ans:
        ans=cap
print(ans)