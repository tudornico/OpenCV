import sys
import pytesseract
import numpy as np
from PIL import Image
sys.path.append('/usr/bin/tesseract')
import cv2

#


if __name__ == '__main__':
    # Press the green button in the gutter to run the script.

    poza1 = 'poza1.jpg'
    poza2 = 'poza2.jpg'
    poza3 = 'Capture.PNG'
    poza4 = 'Capture4.PNG'
    poza5 = 'Capture6.PNG'
    poza6 = 'Capture2.PNG'
    poza7 = 'Crop1.jpg'
    img1 = cv2.imread(poza4)

    # try brigthness  increase
    # img1 = brigthness(poza1)
    # cv2.imshow('Brigthness',img1)
    # cv2.waitKey(0)

    grayImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    # apply treshhold on grayscale img
    cv2.imshow('Gray', grayImg)
    cv2.waitKey(0)

    filtered = cv2.bilateralFilter(grayImg, 7, 30, 100,cv2.BORDER_DEFAULT)

    _, thresh1 = cv2.threshold(filtered, 150, 220, cv2.THRESH_BINARY_INV)  # nice\
    cv2.imshow('thresh', thresh1)
    cv2.waitKey(0)

# thresh1 = cv2.adaptiveThreshold(filtered,300,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,45,25)
# dilate the mask  to make sure  the highlighted area is fully covered
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))

    cv2.imshow('Structure Element', kernel)
    cv2.waitKey(0)

    thresh  = cv2.erode(thresh1,kernel , iterations = 1)
    cv2.imshow('after dialte' , thresh)
    cv2.waitKey(0)


    cleaned = cv2.morphologyEx(thresh , cv2.MORPH_GRADIENT , kernel , iterations = 2)
    cv2.imshow('after ex',cleaned)
    cv2.waitKey(0)


    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    text1 = pytesseract.image_to_string(cleaned, lang='lets', config='--psm 6 -c tessedit_char_whitelist="0123456789"')
    print(text1)
    cv2.imshow('iamge' , cleaned)
    cv2.waitKey(0)