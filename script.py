import pyautogui, time
print("STARTING IN 15 SECONDS! SWITCH TO WHATSAPP WEB!")
time.sleep(15)
f = open("beemovescript.txt", 'r')
for word in f:
 pyautogui.typewrite(word)
 print(word)
 pyautogui.press("enter")
