from pynput.keyboard import Key, Controller as KeyCTR
from pynput.mouse import Button, Controller as MouseCTR
import time

mouse = MouseCTR()
keyboard = KeyCTR()

msg = "Can I please receive an invoice for this months statements \n\n\nKind Regards \nMalcom Thonger"
urlBar = (244, 50)
url = "https://www.vegaschool.com/assist/"
scrollStart = (1359, 213)
scrollEnd = (1358, 315)
scrollEnd2 = (1354, 534)
scrollEnd3 = (1361, 622)
financeBtn = (1097, 589)
invoiceBtn = (1094, 696)
studentNumPos = (750, 464)
studentNum = "st10074559"
submitBtn = (1011, 464)
messageField = (620, 264)
finalBtn = (781, 605)

#time.sleep(5)
for i in range(5):
    print(i)
    time.sleep(1)

def main():
    #Getting to the website
    mouse.position = urlBar
    time.sleep(1)
    mouse.click(Button.left)
    time.sleep(1)
    keyboard.type(url)
    time.sleep(1)
    keyboard.press(Key.enter)
    time.sleep(1)

    #Navigating the website
    mouse.position = scrollStart
    time.sleep(1)
    mouse.press(Button.left)
    time.sleep(1)
    mouse.position = scrollEnd
    time.sleep(1)
    mouse.release(Button.left)
    time.sleep(1)

    #opening the acedemicOperationsBtn
    mouse.position = financeBtn
    time.sleep(1)
    mouse.click(Button.left)
    
    #opening the InvoiceQuery
    mouse.position = invoiceBtn
    time.sleep(1)
    mouse.click(Button.left)
    time.sleep(1)

    #scrolling
    mouse.position = scrollStart
    time.sleep(1)
    mouse.press(Button.left)
    time.sleep(1)
    mouse.position = scrollEnd2
    time.sleep(1)
    mouse.release(Button.left)
    time.sleep(1)

    #entering the student number
    mouse.position = studentNumPos
    time.sleep(1)
    mouse.click(Button.left)
    time.sleep(1)
    keyboard.type(studentNum)
    time.sleep(1)
    mouse.position = submitBtn
    time.sleep(1)
    mouse.click(Button.left)
    time.sleep(1)

    #scrolling
    mouse.position = scrollStart
    time.sleep(1)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)
    time.sleep(1)
    mouse.press(Button.left)
    time.sleep(1)
    mouse.position = scrollEnd3
    time.sleep(1)
    mouse.release(Button.left)
    time.sleep(1)

    #message
    mouse.position = messageField
    time.sleep(1)
    mouse.click(Button.left)
    time.sleep(1)
    keyboard.type(msg)
    time.sleep(1)

    mouse.position = finalBtn
    time.sleep(1)
    #mouse.click(Button.left)
    return

if __name__ == "__main__":
    main()