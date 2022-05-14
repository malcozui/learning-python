from turtle import st
from pynput.keyboard import Key, Controller
import time

keyboard = Controller

def press_keys(char: str):
    keyboard.press(char)
    keyboard.release(char)

def press_keycode(keycode: Key):
    keyboard.press(keycode)
    keyboard.release(keycode)

def type_string(string: str):
    keyboard.type(string)

def realistic_typing_string(string: str):
    for char in string:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)

# time delay to move my cursor to a notepad window.
time.sleep(2)

press_keys("b")

press_keycode(Key.cmd)

type_string("penis man")

realistic_typing_string("Hello World!")
#windows key is Key.cmd