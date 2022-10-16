from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
d=defaultdict(int)
for i in a:
    d[i]+=1
print(max(d.values()),len(d))