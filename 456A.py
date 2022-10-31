n=int(input())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
data.sort(key=lambda x:x[0])
flag=0
for i in range(1,n):
    if data[i][1]<data[i-1][1]:
        flag=1
        break
if flag:
    print("Happy Alex")
else:
    print("Poor Alex")