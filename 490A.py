from collections import Counter

n=int(input())
a=list(map(int,input().split()))
if 1 in a and 2 in a and 3 in a:
    c=Counter(a).most_common()[-1][1]
    data=[]
    for i in range(c):
        one=a.index(1)
        two=a.index(2)
        three=a.index(3)
        data.append([one+1,two+1,three+1])
        a[one]=4
        a[two]=4
        a[three]=4
    print(c)
    for i in data:
        print(*i)
else:
    print(0)