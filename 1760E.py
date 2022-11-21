class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        o,z=-1,-1
        for i in range(n):
            if a[i]==0:
                z=i
                break
        for i in range(n-1,-1,-1):
            if a[i]==1:
                o=i
                break
        c=a.count(0)
        data=[]
        for i in a:
            if i==0:
                c-=1
            data.append(c)
        if o==-1 or z==-1:
            print(n-1)
            return
        ans1,ans2,ans3=0,0,0
        for i in range(n-1):
            if a[i]==1:
                ans1+=data[i]
        a[o]=0
        c=a.count(0)
        data=[]
        for i in a:
            if i==0:
                c-=1
            data.append(c)
        for i in range(n-1):
            if a[i]==1:
                ans2+=data[i]
        a[o]=1
        a[z]=1
        c=a.count(0)
        data=[]
        for i in a:
            if i==0:
                c-=1
            data.append(c)
        for i in range(n-1):
            if a[i]==1:
                ans3+=data[i]
        print(max(ans1,ans2,ans3))

obj=solve()