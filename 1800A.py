class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        t=input().lower()
        s=set(t)
        if len(s)==4 and ('m' in s) and ('e' in s) and ('o' in s) and ('w' in s):
            s=set()
            for i in t:
                if i=='m':
                    if ('e' not in s) and ('o' not in s) and ('w' not in s):
                        s.add('m')
                    else:
                        print("NO")
                        return
                if i=='e':
                    if ('m' in s) and ('o' not in s) and ('w' not in s):
                        s.add('e')
                    else:
                        print("NO")
                        return
                if i=='o':
                    if ('m' in s) and ('e' in s) and ('w' not in s):
                        s.add('o')
                    else:
                        print("NO")
                        return
                if i=='w':
                    if ('e' in s) and ('o' in s) and ('m' in s):
                        s.add('w')
                    else:
                        print("NO")
                        return
            print("YES")
        else:
            print("NO")
 
obj=solve()