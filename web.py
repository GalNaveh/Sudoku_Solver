# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys


# location = 0
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
# driver.get('https://sudoku.com/evil/')
# driver.implicitly_wait(2)
# driver.find_element_by_xpath('//*[@id="banner-close"]').click()
# driver.implicitly_wait(2)

# location = 0.1
# driver.implicitly_wait(5)
# driver.find_element_by_xpath('//*[@id="game"]/canvas').click()
# location = 1
# driver.find_element_by_xpath('//body').send_keys(Keys.NUMPAD1)
# driver.implicitly_wait(5)
# location = 2
# driver.find_element_by_xpath('//body').send_keys(Keys.BACKSPACE)
# driver.implicitly_wait(5)
# location = 3

# with open('sudoku.png', 'wb') as file:
# #identify image to be captured
#     l = driver.find_element_by_xpath('//*[@id="game"]/canvas')
#     driver.find_element_by_xpath('//*[@id="game"]/canvas').click()
# #write file
#     location = 4
#     file.write(l.screenshot_as_png)
# driver.implicitly_wait(10)

# location = 5

y = int(round(11.77,2))
print(y)