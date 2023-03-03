class solve:
    def __init__(self):
        s=input()
        ans=""
        d={ "+":"1010", "-":"1011", "[":"1110", "]":"1111", "<":"1001", ">":"1000", ".":"1100", ",":"1101"}
        for i in s:
            ans+=d[i]
        ans=int(ans,2)
        print(ans%1000003)
 
obj=solve()