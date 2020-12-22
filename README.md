# Text spammer

## BADGES!!
![Codacy Badge](https://img.shields.io/codacy/grade/39041de8660e49b78906fa214cf2f897)
![shields.io](https://img.shields.io/discord/777924198655852555)
![shields.io](https://img.shields.io/github/languages/code-size/ilikecheesybread/text-spammer)
![shields.io is super cool](https://img.shields.io/github/downloads/ilikecheesybread/text-spammer/total)
![shields.io](https://img.shields.io/github/license/ilikecheesybread/text-spammer)
![shields.io](https://img.shields.io/github/watchers/ilikecheesybread/text-spammer?label=Watch%20me&style=social)
![shields.io](https://img.shields.io/website?down_color=grey&down_message=Offline&up_message=Online&url=https%3A%2F%2Filikecheesybread.github.io%2Ftext-spammer%2F)
![shields.io](https://img.shields.io/badge/Built%20with-love-red)

Hey, you're probably looking at this repo on GitHub Pages (ilikecheesybread.github.io) Sooo some of the pointers might not work out for you (you might want to visit [this page](https://github.com/ilikecheesybread/text-spammer/issues "this page") for some pre-made help) but I'll try to break this down as much as possible.

## Installation

First, you are gonna need some things - these will come in handy if I make any other Python programs - using Python. You can download it for free from [here.](https://www.python.org/downloads/ "here.") Once that's done, installation should be a breese. Just type `pip install PyAutoGUI` into your command prompt (Windows key and R, then type `cmd`) and finally download the latest release from [right here.](https://github.com/ilikecheesybread/text-spammer/releases "right here.")

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
