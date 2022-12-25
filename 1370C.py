class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        if n==1:
            print("FastestFinger")
            return
        two=0
        while n%2==0:
            two+=1
            n//=2
        flag=0
        i=2
        while i*i<=n:
            if n%i==0:
                flag=1
                break
            i+=1
        if (n==1 and two!=1) or (n!=1 and two==1 and flag==0):
            print("FastestFinger")
        else:
            print("Ashishgup")
 
obj=solve()