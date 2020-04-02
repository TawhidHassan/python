userName=input("enter you name: ")

i=0
temp_var=""

while i<len(userName):
    if userName[i] not in temp_var:
        temp_var+=userName[i]
        print(f"{userName[i]} : {userName.count(userName[i])}")
    i+=1