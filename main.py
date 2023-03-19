import PIL
import sys

import pytesseract

sys.path.append('/usr/bin/tesseract')
import cv2

if __name__ == '__main__':
    # Press the green button in the gutter to run the script.

    poza1 = 'poza1.jpg'
    poza2 = 'poza2.jpg'
    poza3 = 'Capture.PNG'
    poza4 = 'Capture4.PNG'
    poza5 = 'Capture6.PNG'

    img1 = cv2.imread(poza1)

    grayImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    # apply treshhold on grayscale img

    filtered = cv2.bilateralFilter(grayImg, 7, 15, 305)

    _, thresh1 = cv2.threshold(filtered, 150, 220, cv2.THRESH_BINARY_INV)  # nice

# thresh1 = cv2.adaptiveThreshold(filtered,300,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,45,25)
# cv2.imshow('Tresh Binary', thresh)
# cv2.waitKey(0)
#
# cv2.imshow('Tresh Binary INV', thresh1)
# cv2.waitKey(0)
#
# cv2.imshow('Tresh TRUNC', thresh2)
# cv2.waitKey(0)
#
# cv2.imshow('Tresh To Zero', thresh3)
# cv2.waitKey(0)
#
#
# cv2.imshow('Tresh to Zero inv', thresh4)
# cv2.waitKey(0)
# dilate the mask  to make sure  the highlighted area is fully covered
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
thresh = cv2.dilate(thresh1, kernel)

#contoures with largest area
#contoures, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contoures = cv2.Canny(thresh1,100,200)
cv2.imshow('Edges',contoures)
cv2.waitKey(0)
blur = cv2.GaussianBlur(thresh1 , (5,5) , 0)
# largestContour = max(contoures, key=cv2.contourArea)
edges = cv2.Canny(blur,100,200)
x, y, w, h = cv2.boundingRect(edges)
print(x, y, h, w)
crop = thresh[y:y + h, x: x + w]

cv2.imshow('image window', crop)
cv2.waitKey(0)
