from collections import Counter

class solve:
    def __init__(self):
        s=input()
        k=int(input())
        c=Counter(s).most_common()[::-1]
        count=0
        rem=set()
        for i in c:
            if i[1]<=k:
                k-=i[1]
                rem.add(i[0])
            else:
                count+=1
        ans=""
        for i in s:
            if i not in rem:
                ans+=i
        print(count)
        print(ans)

obj=solve()