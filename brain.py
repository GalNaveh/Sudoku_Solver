from Solver import solved_board, visual
from test_image_split import tile
from read_tiles import read_board
import pyautogui
import time

dir_in = r'C:\Users\galna\OneDrive\Documents\Python\sudoku_improved'
dir_out = r'C:\Users\galna\OneDrive\Documents\Python\sudoku_improved\image_split'
filename = 'sudoku.png'

pyautogui.typewrite(['win', 'g', 'o','o','g','l','e', 'enter'], interval=0.1)
pyautogui.moveTo(543, 605, duration=2)
time.sleep(2)
pyautogui.click()
time.sleep(1)
pyautogui.click(x=1212, y=104,clicks=1,button='left')
time.sleep(1)
pyautogui.click()
pyautogui.typewrite('https://sudoku.com/evil/\n', interval=0.1)

pyautogui.typewrite(['enter'],interval=0.1)
time.sleep(5)
im = pyautogui.screenshot('sudoku.png',region=(161,358, 636, 636))

#calculation
tile(filename, dir_in, dir_out)
input_board = read_board()
visual(input_board)
output_board = solved_board(input_board)
print('#' * 30)
visual(output_board)

column = ['386','463','529','607','681',"734" ,"814","891","972"]
x_spot = 191
#data input
pyautogui.click(x=1932, y=40,clicks=1,button='left')
time.sleep(1)
for i in range(9):
    j = column[i]
    pyautogui.click(x=x_spot, y=j,clicks=1,button='left')
    for z in range(9):
        number = str(output_board[i][z])
        pyautogui.typewrite(number)
        time.sleep(0.01)
        pyautogui.typewrite(["right"])
        time.sleep(0.01)
