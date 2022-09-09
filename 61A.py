s1=input()
s2=input()
n=len(s1)
ans=""
for i in range(n):
    if s1[i]!=s2[i]:
        ans+="1"
    else:
        ans+="0"
print(ans)