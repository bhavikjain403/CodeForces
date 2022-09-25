d=input()
s=input()
data="qwertyuiopasdfghjkl;zxcvbnm,./"
ans=""
if d=="R":
    for i in s:
        ans+=data[data.index(i)-1]
else:
    for i in s:
        ans+=data[data.index(i)+1]
print(ans)