print("Started")

import pyautogui
import time

time.sleep(4)

# with open("D:\\Study material\\NIIT\\Pythonfile\\Linklist\\typeautomate.txt", 'r') as file:
with open("typeautomate.txt", 'r') as file:
    text = file.read()

pyautogui.write(text)
# for i in range(len(text)):
# 	pyautogui.typewrite(text[i])
print(text)
input("----------Copy Done----------")
