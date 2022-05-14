from turtle import st
from pynput.keyboard import Key, Controller
import time

keyboard = Controller

def press_keys(char: chr):
    keyboard.press(char)
    keyboard.release(char)

def press_keycode(keycode):
    keyboard.press(keycode)
    keyboard.release(keycode)

def type_string(string):
    keyboard.type(string)

def realistic_typing_string(string):
    for char in string:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)

press_keys()
#windows key is Key.cmd