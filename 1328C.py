class solve:
    def __init__(self):
        for i in range(int(input())):
            self.solution()
 
    def solution(self):
        n=int(input())
        x=input()
        a,b="",""
        flag=0
        for i in x:
            if flag:
                if i=="0":
                    a+="0"
                    b+="0"
                elif i=="1":
                    a+="0"
                    b+="1"
                else:
                    a+="0"
                    b+="2"
            else:
                if i=="0":
                    a+="0"
                    b+="0"
                elif i=="1":
                    a+="1"
                    b+="0"
                    flag=1
                else:
                    a+="1"
                    b+="1"
        print(a)
        print(b)

obj=solve()