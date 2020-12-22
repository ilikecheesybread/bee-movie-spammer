# Text spammer
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f8b9505eb05842829a37d50ca669f6c7)](https://app.codacy.com/gh/ilikecheesybread/text-spammer?utm_source=github.com&utm_medium=referral&utm_content=ilikecheesybread/text-spammer&utm_campaign=Badge_Grade)

Hey, you're probably looking at this repo on GitHub Pages (ilikecheesybread.github.io) Sooo some of the pointers might not work out for you (you might want to visit [this page](https://github.com/ilikecheesybread/text-spammer/issues "this page") for some pre-made help) but I'll try to break this down as much as possible.

## Installation

First, you are gonna need some things - these will come in handy if I make any other Python programs - like Python. You can download it for free from [here.](https://www.python.org/downloads/ "here.") Once that's done, installation should be a breese. Just type `pip install PyAutoGUI` into your command prompt (Windows key and R, then type `cmd`) and finally download the latest release from [right here.](https://github.com/ilikecheesybread/text-spammer/releases "right here.")

FINALLY you've installed it, but now what?

### Running the software

Right, this should be fairly straightforeward. Just find the program on your disk [usually in the `%PROGRAMDATA%` or `%APPDATA%` folders [just type them directly into the file explorer's address bar]] and run `script.py` on Python's IDLE. Wait around 10 seconds (allowing you to open Discord / WhatsApp Desktop) and each line will be typed.

### Variables

There are some things that you can change such as the time between each message (to prevent being ratelimited) or the actual .txt file that the program is reading. To change the time between each message, simply edit the `time.sleep(2)` line, making sure to remove the '#' before the line.
````python
for word in source:
    pyautogui.typewrite(word)
    print(word)
    pyautogui.press("enter")
    #time.sleep(2)
````
To change the file that is being read, simply locate the line:
```python
source = open("nevergonnagiveyouup.txt", 'r')
```
and change the .txt file. It has been defaulted to Rick Astley's Never gonna give you up.

### Contact

If there are ANY problems, please don't hesitate to add a new issue on GitHub or DM me on Discord. Have fun!

#### Disclaimer
If your account get's banned for sending lots of messages in a short amount of time, you take full responsibilty becasue you downloaded any of the aforementioned programs. Enjoy at your own risk.
