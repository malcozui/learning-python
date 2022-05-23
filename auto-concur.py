from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyController
import time

mouse = Controller()
keyboard = KeyController()
# (360, 15)
# (1615, 915)
if __name__ == "__main__":
    time.sleep(5)
    mouse.position = (360, 15)
    mouse.click(Button.left, 1)
    time.sleep(0.1)
    mouse.position = (1615, 915)
    mouse.click(Button.left, 1)
    keyboard.type("I concur.")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
