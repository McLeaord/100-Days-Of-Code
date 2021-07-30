# sorting the list in ascending orer
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = []

while list:
    min = list[0]  
    for x in list: 
        if x > min:
            min = x
    n.append(min)
    list.remove(min)    

print(n)