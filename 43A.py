from collections import defaultdict

d=defaultdict(int)
n=int(input())
for i in range(n):
    s=input()
    d[s]+=1
print(max(d, key=d.get))