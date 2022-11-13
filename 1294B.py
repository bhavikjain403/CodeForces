class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()

    def solution(self):
        n=int(input())
        data=[]
        for i in range(n):
            data.append(list(map(int,input().split())))
        data.sort(key=lambda x:(x[1],x[0]))
        i,ans,x,y=0,"",0,0
        while i<n:
            if x<=data[i][0] and y<=data[i][1]:
                ans+="R"*(data[i][0]-x)
                ans+="U"*(data[i][1]-y)
                x,y=data[i][0],data[i][1]
            else:
                print("NO")
                return
            i+=1
        print("YES")
        print(ans)

obj=solve()