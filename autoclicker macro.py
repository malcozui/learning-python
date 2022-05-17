from pynput import mouse
from pynput import keyboard
from time import sleep

mouse1 = mouse.Controller()
mouse_b = mouse.Button
keyboard1 = keyboard.Controller()
keyboard_keys = keyboard.Key

def autoclicker(number_of_clicks: int, sleep_time: float = 0.005):
    for i in range(number_of_clicks):
        mouse.Controller().click(mouse_b.left, 1)
        sleep(sleep_time)

inp = input("how many clicks would you like? \n")

sleep(5)
autoclicker(int(inp))