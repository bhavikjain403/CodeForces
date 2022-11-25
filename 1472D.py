class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
            
    def solution(self):
        n=int(input())
        a=list(map(int,input().split()))
        a.sort(reverse=True)
        ans=0
        for i in range(n):
            if i%2:
                if a[i]%2:
                    ans-=a[i]
            else:
                if a[i]%2==0:
                    ans+=a[i]
        if ans==0:
            print("Tie")
        elif ans>0:
            print("Alice")
        else:
            print("Bob")

obj=solve()