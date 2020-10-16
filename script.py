#You need to have pyautogui installed.
import pyautogui, time

print("Running... Open WhatsApp Web or other...")

time.sleep(10)
beemoviescript = open("source.txt", 'r')

for word in beemoviescript:
    pyautogui.typewrite(word)
    print(word)
    pyautogui.press("enter")
