a=input()
b=input()
c=str(int(a)+int(b))
c=c.replace("0","")
a=a.replace("0","")
b=b.replace("0","")
if int(c)==int(a)+int(b):
    print("YES")
else:
    print("NO")