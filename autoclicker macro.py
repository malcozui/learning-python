from pynput import mouse
from pynput import keyboard
from time import sleep

mouse1 = mouse.Controller()
mouse_b = mouse.Button
keyboard1 = keyboard.Controller()
keyboard_keys = keyboard.Key

for i in range(1):
    mouse1.click(mouse_b.left, 1)
    sleep(0.05)