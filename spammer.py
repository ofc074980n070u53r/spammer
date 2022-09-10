import pyautogui as pt
import time

input = input()
print("hai sette secondi per selezionare il testo")
time.sleep(7)

for i in range(100):
    pt.write(input)
    time.sleep(0.5)
    pt.press("enter")
