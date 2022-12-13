class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
            
    def solution(self):
        n=int(input())
        s=set()
        i=2
        while i*i<=n:
            if n%i==0 and (i not in s):
                s.add(i)
                n//=i
                break
            i+=1
        i=2
        while i*i<=n:
            if n%i==0 and (i not in s):
                s.add(i)
                n//=i
                break
            i+=1
        if len(s)<2 or (n in s) or n==1:
            print("NO")
        else:
            print("YES")
            for i in s:
                print(i,end=" ")
            print(n)

obj=solve()