class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        temp=0
        b=sorted(a,reverse=True)
        neg=0
        for i in b:
            if i>0:
                temp+=1
                print(temp,end=" ")
            else:
                temp-=1
                print(temp,end=" ")
                neg+=1
        print()
        for i in range(neg):
            print("1 0",end=" ")
        temp=1
        for i in range(n-2*neg):
            print(temp,end=" ")
            temp+=1
        print()
 
obj=solve()