class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
    
    def solution(self):
        n=int(input())
        a=input()
        cnt=a.count("*")
        val,idx=-1,-1
        for i in range(n):
            if a[i]=="*":
                val+=1
                if val==cnt//2:
                    idx=i
        ans=0
        val=idx-cnt//2
        for i in range(n):
            if a[i]=="*":
                ans+=abs(val-i)
                val+=1
        print(ans)

obj=solve()