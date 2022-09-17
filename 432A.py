n,k=map(int,input().split())
a=list(map(int,input().split()))
a=list(filter(lambda x:x<=5-k,a))
print(len(a)//3)