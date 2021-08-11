list = []
n = int(input("enter no of elements"))
print("enter elements of the list")

for items in range(n):
    a=int(input(""))
    list.append(a)

print("list is",list)

for i in range(len(list)):  
    for j in range (0,len(list)-1):
        if (list[j]>list[j+1]):
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp  

print("sorted list is:",list)