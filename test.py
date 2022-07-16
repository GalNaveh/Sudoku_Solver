import cv2
import pytesseract
import numpy as np
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
import os
import easyocr
import shutil
from PIL import Image
reader = easyocr.Reader(["en"])

def test_board():
    board = []
    image_name = 'sudoku_31.png'
    img = cv2.imread("image_split\\"+image_name)
    img = cv2.medianBlur(img, 3)
    text = pytesseract.image_to_string(img,config='--psm 10')
    print(text)

test_board()
dir_in = r'C:\Users\galna\OneDrive\Documents\Python\sudoku_improved'
dir_out = r'C:\Users\galna\OneDrive\Documents\Python\sudoku_improved\image_split'
filename = 'sudoku.png'

def test2_board():
    image_name = 'sudoku_31.png'
    for filenames in os.listdir(dir_out):
        filepath = os.path.join(dir_out, filenames)
        try:
            shutil.rmtree(filepath)
        except OSError:
            os.remove(filepath)

    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    
    width, height = img.size
 
    # Setting the points for cropped image
    left = 0
    top = (height /10)
    right = width
    bottom = height  - (height /10)
    
    # Cropped image of above dimension
    # (It will not change original image)
    # img = cv2.imread("image_split\\"+image_name)
    img1 = img.crop((left, top, right, bottom))
    # img1 = cv2.medianBlur(img1, 3)
    text = reader.recognize(img1, detail=0)[0]
    print(text)

test2_board()

