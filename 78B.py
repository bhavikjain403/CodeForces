n=int(input())
for i in range(n//7):
    print("ROYGBIV",end="")
data=["","G","GB","YGB","YGBI","OYGBI","OYGBIV"]
print(data[n%7])