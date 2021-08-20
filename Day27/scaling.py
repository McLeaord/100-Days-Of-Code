import cv2
import numpy as np

FILE_NAME = 'volleyball.jpg'
try:
    img = cv2.imread(FILE_NAME)


(height, width) = img.shape[:2]
(rows, cols) = img.shape[:2]


res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation = cv2.INTER_CUBIC)
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
res = cv2.warpAffine(img, M, (cols, rows))

cv2.imwrite('result.jpg', res:
except IOError:
    print ('Error while reading files')
