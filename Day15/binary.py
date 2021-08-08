num = int(input('Enter any decimal number: '))


def DecimalBinary(n): 
    if n >= 1:
        DecimalBinary(n // 2)
    print(n % 2, end = '')
 



print('Binary value: ')
DecimalBinary(num)
    

 