list=[]
str=""
while(1):
    str = input("Enter item : ")
    if(str == "done"):
        break
    else:
        list.append(str)
        print(f"{str} added to list")
print(list)        