class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        c,data=0,[0]*n
        for i in range(n):
            while a[i]%2==0:
                a[i]//=2
                c+=1
            temp,v=0,i+1
            while v%2==0:
                v//=2
                temp+=1
            data[i]=temp
        data.sort(reverse=True)
        if c>=n:
            print(0)
            return
        ans=0
        for i in data:
            c+=i
            ans+=1
            if c>=n:
                print(ans)
                return
        print(-1)
 
obj=solve()