import cv2
 
img = cv2.imread("car.jpg", cv2.IMREAD_UNCHANGED)
dimensions = img.shape
 
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
 
print("Image Dimension    : ",dimensions)
print("Image Height       : ",height)
print("Image Width        : ",width)
print("Number of Channels : ",channels)