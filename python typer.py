from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

class Key_Functions:
    def press_keys(char: str):
        keyboard.press(char)
        keyboard.release(char)

    def press_keycode(keycode: Key):
        keyboard.press(keycode)
        keyboard.release(keycode)

    def type_string(string: str):
        keyboard.type(string)

    def realistic_typing_string(string: str, time_between_keystrokes: float = 0.12):
        for char in string:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(time_between_keystrokes)
    
    def open_application(app: str):
        kf.press_keycode(Key.cmd)
        time.sleep(.1)
        kf.type_string(app)
        time.sleep(.1)
        kf.press_keycode(Key.enter)
        time.sleep(.2)


kf = Key_Functions

def notepad_typer():
    kf.open_application("notepad")
    # Now notepad is open.
    kf.realistic_typing_string("Whatever you'd like to type to the user.", 0.05)

def cmd_open():
    kf.open_application("cmd")
    time.sleep(.1)
    # Now cmd is open, not in admin though :(
    kf.realistic_typing_string("color a && cls && cmd")
    kf.press_keycode(Key.enter)
    time.sleep(.1)
    kf.type_string("tree")
    kf.press_keycode(Key.enter)

# notepad_typer()
# cmd_open()
