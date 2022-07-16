from PIL import Image
from itertools import product
import os
import shutil
dir_in = r'C:\Users\galna\OneDrive\Documents\Python\sudoku_improved'
dir_out = r'C:\Users\galna\OneDrive\Documents\Python\sudoku_improved\image_split'
filename = 'sudoku.png'

img = Image.open('sudoku.png')

def tile(filename, dir_in, dir_out):
    x = 0
    for filenames in os.listdir(dir_out):
        filepath = os.path.join(dir_out, filenames)
        try:
            shutil.rmtree(filepath)
        except OSError:
            os.remove(filepath)

    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size
    d = int(w / 9)
    grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
    for i, j in grid:
        box = (j, i, j+d, i+d)
        out = os.path.join(dir_out, f'{name}_{x}{ext}')
        x +=1
        img.crop(box).save(out)

tile(filename, dir_in, dir_out)