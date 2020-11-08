#You need to have pyautogui installed.
import pyautogui, time

print("Running... Open WhatsApp Web or other...")

time.sleep(10)
source = open("source.txt", 'r')

for word in source:
    pyautogui.typewrite(word)
    print(word)
    pyautogui.press("enter")
    #time.sleep(2)
