class solve:
    def __init__(self):
        n=int(input())
        dx={}
        dy={}
        repeat={}
        ans=0
        for i in range(n):
            p,q=map(int,input().split())
            ans+=dx.get(p,0)+dy.get(q,0)-repeat.get((p,q),0)
            if dx.get(p,0):
                dx[p]+=1
            else:
                dx[p]=1
            if dy.get(q,0):
                dy[q]+=1
            else:
                dy[q]=1
            if repeat.get((p,q),0):
                repeat[(p,q)]+=1
            else:
                repeat[(p,q)]=1
        print(ans)

obj=solve()