a1,a2,a3=map(int,input().split())
b1,b2,b3=map(int,input().split())
n=int(input())
s1=(a1+a2+a3)//5
s2=(b1+b2+b3)//10
if (a1+a2+a3)%5:
    s1+=1
if (b1+b2+b3)%10:
    s2+=1
if s1+s2<=n:
    print("YES")
else:
    print("NO")