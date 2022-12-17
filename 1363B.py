class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
            
    def solution(self):
        s=input()
        one=s.count("1")
        zero=s.count("0")
        ans=min(one,zero)
        x,y=0,0
        for i in s:
            if i=="1":
                x+=1
                one-=1
            else:
                y+=1
                zero-=1
            ans=min(ans,x+zero,y+one)
        print(ans)


obj=solve()