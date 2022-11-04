class solve:
    def __init__(self):
        k=int(input())
        n=int(input())
        s,sums=str(n),0
        l=len(s)
        data=[0]*l
        for i in range(l):
            t=int(s[i])
            sums+=t
            if sums>=k:
                print("0")
                return
            data[i]=9-t
        if sums>=k:
            print("0")
        else:
            data.sort(reverse=True)
            i,ans=0,0
            while sums<k:
                sums+=data[i]
                ans+=1
                i+=1
            print(ans)

obj=solve()