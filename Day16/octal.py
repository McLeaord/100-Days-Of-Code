table = ["0", "1","2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
num = int(input('Enter any decimal number: '))

octal = ''

while(num>0):
    x = num%8
    octal = table[x]+ octal
    num = num//8
    
print("Octal is : ",octal)

 