table = ["0", "1","2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
num = int(input('Enter any decimal number: '))

hexadecimal = ''

while(num>0):
    x = num%16
    hexadecimal = table[x]+ hexadecimal
    num = num//16
    
print("Hexadecimal: ",hexadecimal)

 