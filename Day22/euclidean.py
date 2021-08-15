import math

print("   ****** welcome TO Euclidean Caliculator *****  ")
print()

print("Enter Point A")
x1, y1 = map(int, input().split())

print()

print("Enter point B")
x2, y2 = map(int, input().split())
dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print()

print("The Euclidean Distance is " + str(dist))

print()

print("   ***** Thank You *****   ")
print()