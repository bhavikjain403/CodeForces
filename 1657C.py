from queue import deque

class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        s=input()
        op=0
        i=0
        while i<n:
            if i==n-1:
                print(op,1)
                return
            if s[i]==")":
                flag=1
                for j in range(i+1,n):
                    if s[j]==")":
                        i=j+1
                        op+=1
                        flag=0
                        break
                if flag:
                    print(op,n-i)
                    return
            else:
                op+=1
                i+=2
        print(op,n-i)

obj=solve()