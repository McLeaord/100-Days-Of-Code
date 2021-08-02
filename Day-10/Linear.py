list = [10,20,30,40,50]
key = 20

def linear(list,n,key):
    for i in range(0,n):
        if (list[i] == key):
            return i

n = len(list)
res = linear(list,n,key)
if(res == -1):
    print("not found")
else:
        print("found at: ",res)
