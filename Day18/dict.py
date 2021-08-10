colors = {1:'Red', 3:'Green', 5:'Black' , 2:'White', 4:'Pink'}

def sort(d, reverse = True):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

print("Given Elements : ")
print(colors)
print()
print("Ascending Order : ")
print(sort(colors,False))
print()
print("Descending Order : ")
print(sort(colors, True))

