class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        c=0
        e=0
        data=[]
        dataeven=[]
        for i in range(n):
            if a[i]%2:
                c+=1
                data.append(i+1)
            else:
                e+=1
                dataeven.append(i+1)
            if c>=3:
                break
        if c>=3:
            print("YES")
            print(data[0],data[1],data[2])
        elif c>=1 and e>=2:
            print("YES")
            print(data[0],dataeven[0],dataeven[1])
        else:
            print("NO")
 
obj=solve()