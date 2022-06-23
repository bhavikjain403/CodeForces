l = []
for i in range(5):
    l.append(list(map(int,input().split())))
for i in range(5):
    for j in range(5):
        if l[i][j]==1:
            x,y=i,j
            break
print(abs(x-2)+abs(y-2))