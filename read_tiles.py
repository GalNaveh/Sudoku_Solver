import cv2
import pytesseract
import numpy as np
import time
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
import easyocr
reader = easyocr.Reader(["en"])




def read_board():
    board = []
    for i in range(81):
        image_name = 'sudoku_{}.png'.format(str(i))
        y = int(12)
        x = y
        w = int(47.11)
        h=w
        img = cv2.imread("image_split\\"+image_name)
        img = img[y:(y+h), (x):(x+w)]
        img = cv2.medianBlur(img, 3)
        text = reader.recognize(img, detail=0)[0]
        board.append(text)
    
    board = fixing_values(board)

    board_array = np.array(board)
    board_array = board_array.reshape(9,9)
    board = board_array.tolist()

    return board

def fixing_values(board):
    clean_board = []
    for i in range(81):
        element = board[i] 
        element = element.replace('\n','')
        element = cleans_erros(element)
        if not element:
            element = 0
        if element:
            element = int(element[0])
        clean_board.append(element)
    return clean_board

def cleans_erros(element):
    temp = []
    
    for i in element:
        try:
            element = int(element)
        except:
            pass
        if isinstance(element, int):
            temp.append(i)

    if len(temp) == 1:
        return temp
    
    elif len(temp) >= 1:
        x = '1'
        while x in temp:
            temp.remove('1') 
    
    if temp:
        temp = temp[0]

    return temp