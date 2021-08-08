table = ["0", "1","2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
num = int(input('Enter any decimal number: '))

binary = ''

while(num>0):
    x = num%2
    binary = table[x]+ binary
    num = num//2
    
print("Binary is : ",binary)

 