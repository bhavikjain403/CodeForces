n=int(input())
a=list(map(int,input().split()))
c=len(list(filter(lambda x:x<0,a)))
if c==0:
    ans=1
else:
    ans=c//2+c%2
print(ans)
neg,x,y=0,0,0
for i in range(n):
    if a[i]<0:
        neg+=1
    x+=1
    if neg==2 and ans>1:
        print(f"{x} ",end="")
        y+=x
        neg,x=0,0
        ans-=1
    elif neg==2 and ans==1:
        break
print(n-y,end="",sep="") 