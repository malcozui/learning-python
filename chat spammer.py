from pynput.mouse import Button, Controller as mCTR
from pynput.keyboard import Key, Controller as kCTR
import time

mouse = mCTR()
keyboard = kCTR()

def initiallise():
    mouse.position = (1630, 915)
    mouse.click(Button.left)

def press_key(key: Key):
    keyboard.press(key)
    keyboard.release(key)

def letter_by_letter(text: str):
    initiallise()
    for char in text:
        if char != " ":
            keyboard.type(char)
            press_key(Key.enter)
            time.sleep(0.2)
        else:
            continue

def spam_by_count(text: str, count: int):
    initiallise()
    for i in range(count):
        keyboard.type(text)
        press_key(Key.enter)
        time.sleep(0.2)

time.sleep(2)

# letter_by_letter("Spam Bot by malcozui. tm.")
spam_by_count("Hello World!", 10)