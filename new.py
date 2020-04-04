# break use

i=0
n=int(input("enter you total sum number: "))
total=0
# for i in range(1,n+1):
#     if i==5:
#         break
#     total+=i
#     print(i)
for i in range(1,n+1):
    if i==5:
        continue
    total+=i
    print(i)
