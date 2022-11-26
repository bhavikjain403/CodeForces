class solve:
    def __init__(self):
        n=input()
        l=len(n)
        ans=""
        i=0
        if n[i]=="9":
            ans+="9"
            i+=1
        while i<l:
            t=int(n[i])
            if t>4:
                ans+=str(9-t)
            else:
                ans+=n[i]
            i+=1
        print(ans)

obj=solve()