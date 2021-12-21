print("Started")
import pyautogui
import time

time.sleep(3)
print("Writing starts")
time.sleep(1)

# with open("D:\\Study material\\NIIT\\Pythonfile\\Linklist\\typeautomate.txt", 'r') as file:
with open("typeautomate.txt", 'r') as file:
    text = file.read()


text = text.replace('\t', '               ')

pyautogui.typewrite(text)
# for i in range(len(text)):
# 	pyautogui.typewrite(text[i])
print(text)
print("----------Copy Done----------")
