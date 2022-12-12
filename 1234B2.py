from collections import deque

class solve:
    def __init__(self):
        n,k=map(int,input().split())
        a=list(map(int,input().split()))
        q=deque()
        l=0
        s=set()
        for i in a:
            if i not in s:
                s.add(i)
                if l<k:
                    l+=1
                else:
                    s.remove(q.pop())
                q.appendleft(i)
        print(l)
        for i in q:
            print(i,end=" ")

obj=solve()