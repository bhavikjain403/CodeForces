s=input()
l=s.lower()
u=s.upper()
n=len(s)
lc,uc=0,0
for i in range(n):
    if s[i]==l[i]:
        lc+=1
    else:
        uc+=1
if lc>=uc:
    print(l)
else:
    print(u)