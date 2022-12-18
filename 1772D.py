class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        flag=1
        for i in range(n-1):
            if a[i]>a[i+1]:
                flag=0
                break
        if flag:
            print("0")
            return
        avg=[0]*(n-1)
        for i in range(0,n-1):
            avg[i]=(a[i]+a[i+1])//2+(a[i]+a[i+1])%2
        for i in avg:
            temp=abs(a[0]-i)
            for j in range(1,n):
                temp2=abs(a[j]-i)
                if temp2<temp:
                    break
                else:
                    temp=temp2
                if j==n-1:
                    print(i)
                    return
        print("-1")
 
obj=solve()