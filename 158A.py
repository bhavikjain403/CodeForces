a = list(map(int, input().split()))
l = list(map(int, input().split()))
c = 0
for i in range(a[0]):
    if l[i]>0 and l[i]>=l[a[1]-1]:
        c+=1
print(c)