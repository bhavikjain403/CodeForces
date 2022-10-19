n=int(input())
a=list(map(int,input().split()))
c,b,bic=0,0,0
for i in range(n):
    if i%3==0:
        c+=a[i]
    elif i%3==1:
        bic+=a[i]
    else:
        b+=a[i]
if max(c,b,bic)==c:
    print("chest")
elif max(c,b,bic)==b:
    print("back") 
else:
    print("biceps")