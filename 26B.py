class solve:
    def __init__(self):
        s=input()
        stack=[]
        ans=0
        for i in s:
            if i=="(":
                stack.append("(")
            else:
                if stack:
                    stack.pop()
                    ans+=1
        print(ans*2)
 
obj=solve()