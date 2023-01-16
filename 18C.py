class solve:
    def __init__(self):
        n=int(input())
        a=list(map(int,input().split()))
        if n==1:
            print("0")
        elif n==2:
            if a[0]==a[1]:
                print("1")
            else:
                print("0")
        else:
            s=sum(a)
            left,right=s-a[n-1],a[n-1]
            ans=0
            if left==right:
                    ans+=1
            for i in range(n-2,0,-1):
                left-=a[i]
                right+=a[i]
                if left==right:
                    ans+=1
            print(ans)
 
obj=solve()