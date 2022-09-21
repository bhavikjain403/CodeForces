n,s=map(int,input().split())
a=list(map(int,input().split()))
if (sum(a)-max(a))<=s:
    print("YES")
else:
    print("NO")