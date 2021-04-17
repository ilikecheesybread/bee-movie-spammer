#You need to have pyautogui installed.
import pyautogui, time

print("Running... Open WhatsApp Web or other...")

time.sleep(5)
source = open("beemovie.txt", 'r')

for word in source:
    pyautogui.typewrite(word)
    print(word)
    pyautogui.press("enter")
    time.sleep(1.1)
