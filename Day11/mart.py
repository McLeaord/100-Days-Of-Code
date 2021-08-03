list1 = ["apple", "banana", "mango", "guva", "orange", "berry", "grapes", "litchi"]
list2 = [40,30,50,5,15,20,40,10]
print("             FRUIT MART       ")
print("-----------------------------------")
print("Fruits Available : ")
print("-----------------------------------")
print(list1)
print("-----------------------------------------------------------------------------------")
key = str(input(" Product        :  "))
x = int(input(" Quantity       :  "))


def search (list1,key):
    for i in range(len(list2)):
        if key == list1[i]:
            print("Price           :  ",x*list2[i])
            print("----------------------------------------------------")
            print("         ****KEEP SHOPPING WIITH US****     ")
            break

        


search (list1,key)