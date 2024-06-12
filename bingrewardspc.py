import pyautogui as pgui
import time


pgui.hotkey('winleft')
time.sleep(3)
pgui.write("Microsoft Edge")
time.sleep(1)
pgui.hotkey('enter')
time.sleep(1)
pgui.write("https://www.bing.com/")
pgui.hotkey('enter')
time.sleep(2)
variavel = 1

for i in range(30): # Número de repetições
    digitador = str(variavel)
    pgui.write(f"{digitador}")
    pgui.hotkey('space')
    time.sleep(1)
    pgui.hotkey('enter')
    time.sleep(5)
    pgui.hotkey('alt', 'd')
    pgui.write("https://www.bing.com/")
    pgui.hotkey('enter')
    time.sleep(1)
    variavel += 1
