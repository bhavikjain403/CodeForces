l=input()
l=l[1:-1]
s=set()
for i in l:
    if i!="," and i!=" ":
        s.add(i)
print(len(s))