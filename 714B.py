class solve:
    def __init__(self):
        n=int(input())
        a=list(map(int,input().split()))
        s=list(set(a))
        l=len(s)
        if l>=4:
            print("NO")
        elif l<=2:
            print("YES")
        else:
            s.sort()
            if s[1]*2==s[0]+s[2]:
                print("YES")
            else:
                print("NO")

obj=solve()