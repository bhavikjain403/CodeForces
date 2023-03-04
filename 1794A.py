class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        a=list(map(str,input().split()))
        if n==2:
            if a[0]==a[1]:
                print("YES")
            else:
                print("NO")
            return
        s1,s2="",""
        for i in a:
            if len(i)==n-1:
                if s1=="":
                    s1=i
                elif s2=="":
                    s2=i
            if s1!="" and s2!="":
                break
        if s1[1:]==s2[:-1]:
            s=s1+s2[-1]
        else:
            s=s2+s1[-1]
        if s==s[::-1]:
            print("YES")
        else:
            print("NO")
 
obj=solve()