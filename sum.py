i = int(input("Enter the Number : ")) 
even = 0
odd = 0

for n in range(i + 1):
    if(n % 2 == 0):
        even = even + n
    else:
        odd = odd + n
       
print("Sum of Even Numbers from 1 to {0} = {1}".format(n, even))
print("Sum of Odd Numbers from 1 to {0} = {1}".format(n, odd))