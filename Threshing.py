import PIL
import sys
import numpy as np
import pytesseract
import math
sys.path.append('/usr/bin/tesseract')
import cv2

if __name__ == '__main__':
    # Press the green button in the gutter to run the script.

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
    w, h = 700, 700
    x = max(0, x - w / 2)
    y = max(0, y - h / 2)
    w = min(w, img1.shape[1] - x)
    h = min(h, img1.shape[0] - y)
    print(math.floor(x) ,math.floor( y) , h , w)
    x = math.floor(x)
    y = math.floor(y)
    h = math.floor(h)
    w = math.floor(w)
    crop = img1[y:y + h, x:x + w]
    cv2.imshow('cropped',crop)
    cv2.waitKey(0)

    _, thresh1 = cv2.threshold(crop, 150, 220, cv2.THRESH_BINARY_INV)  # nice\
    cv2.imshow('thresh', thresh1)
    cv2.waitKey(0)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))

    thresh = cv2.erode(thresh1, kernel, iterations=3)
    cv2.imshow('after erosion', thresh)
    cv2.waitKey(0)

    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel, iterations=3)
    cv2.imshow('after ex', cleaned)
    cv2.waitKey(0)

    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    text1 = pytesseract.image_to_string(cleaned, lang='lets', config='--psm 6 -c tessedit_char_whitelist="0123456789"')
    print(text1)