import PIL
import sys
import numpy as np
import pytesseract
import math
sys.path.append('C:/Program Files/Tesseract-OCR')
import cv2

if __name__ == '__main__':
    # Press the green button in the gutter to run the script.

    #look around and create the base line for new threshhold


    poza1 = 'poza1.jpg'
    poza2 = 'poza2.jpg'
    poza3 = 'Capture2.PNG'
    poza4 = 'Capture4.PNG'
    poza5 = 'Capture6.PNG'
    counter =  'Counter2.jpeg'
    counter1 = 'Counter.jpeg'
    img1 = cv2.imread(counter1, cv2.IMREAD_GRAYSCALE)
    cv2.imshow(' Grayscale', img1)
    cv2.waitKey(0)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img1)
    x, y = max_loc
    w, h = 600, 600
    x = max(0, x - w / 2)
    y = max(0, y - h / 2)
    w = min(w, img1.shape[1] - x)
    h = min(h, img1.shape[0] - y)
    x = math.floor(x)
    y = math.floor(y)
    h = math.floor(h)
    w = math.floor(w)
    crop = img1[y:y + h, x:x + w]
    cv2.imshow('cropped',crop)
    cv2.waitKey(0)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(crop)
    # _, thresh1 = cv2.threshold(crop, 150, 220, cv2.THRESH_BINARY_INV)
    # cv2.imshow('thresh', thresh1)
    # cv2.waitKey(0)
    print(min_val , max_val )
    # we need to find an adaptive way to thresh withouth destroying the numbers on the counter photo

    _, thresh1 = cv2.threshold(crop, max_val-4*min_val, max_val, cv2.THRESH_TOZERO)  # nice
    cv2.imshow('thresh', thresh1)
    cv2.waitKey(0)
    _,thresh1 = cv2.threshold(thresh1 , max_val-4*min_val , max_val, cv2.THRESH_BINARY_INV)
    # Creating a structuring element for each of the numbers in our counter
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 3))

    cv2.imshow('structuring element' , kernel)
    cv2.waitKey(0)
    erode = cv2.erode(thresh1, kernel, iterations=3)
    cv2.imshow('after erosion', erode)
    cv2.waitKey(0)

    dilate = cv2.dilate(erode, kernel, iterations=1)
    cv2.imshow('dilation', dilate)
    cv2.waitKey(0)

    cleaned = cv2.morphologyEx(dilate, cv2.MORPH_TOPHAT, kernel, iterations=4)
    cv2.imshow('after morph', cleaned)
    cv2.waitKey(0)


    pytesseract.pytesseract.tesseract_cmd = r'C://Program Files//Tesseract-OCR//tesseract'
    text1 = pytesseract.image_to_string(cleaned, lang='lets', config='--psm 6 -c tessedit_char_whitelist="0123456789"')
    print(text1)