class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        s=input()
        x,y=0,0
        for i in s:
            if i=="L":
                x-=1
            elif i=="R":
                x+=1
            elif i=="U":
                y+=1
            elif i=="D":
                y-=1
            if x==1 and y==1:
                print("YES")
                return
        print("NO")

obj=solve()