t=int(input())
while t:
    s=input()
    s=list(s)
    n=len(s)
    if n==2:
        print(abs(ord(s[0])-ord(s[1])),2)
        print("1 2")
    else:
        d=dict()
        prev,final=ord(s[0])-96,ord(s[n-1])-96
        for i in range(1,n-1):
            ordi=ord(s[i])-96
            if prev>=final:
                if ordi<=prev and ordi>=final:
                    d[i]=ordi
                else:
                    d[i]=-1
            else:
                if ordi>=prev and ordi<=final:
                    d[i]=ordi
                else:
                    d[i]=1000
        if prev>=final:
            d=sorted(d.items(), key=lambda x: x[1],reverse=True)
        else:
            d=sorted(d.items(), key=lambda x: x[1])
        i,m=0,1
        ans=[1]
        for i in d:
            if i[1]==1000 or i[1]==-1:
                break
            else:
                m+=1
                ans.append(i[0]+1)
        ans.append(n)
        print(abs(ord(s[0])-ord(s[n-1])),m+1)
        print(*ans)
    t-=1