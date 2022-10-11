s,n=map(int,input().split())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
data.sort(key=lambda x:x[0])
flag=1
for i in data:
    if i[0]>=s:
        flag=0
        print("NO")
        break
    else:
        s+=i[1]
if flag:
    print("YES")