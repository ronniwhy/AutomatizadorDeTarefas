import pyautogui as pgui
import time


pgui.hotkey('winleft')
print('Pressionando a tecla: "winleft"...')
time.sleep(3)
pgui.write("Microsoft Edge")
print('Digitando: "Microsoft Edge"...')
time.sleep(1)
pgui.hotkey('enter')
print('Pressionando a tecla: "enter"...')
time.sleep(1)
pgui.write("https://www.bing.com/")
print('Digitando: "https://www.bing.com/"...')
pgui.hotkey('enter')
print('Pressionando a tecla: "enter"')
time.sleep(2)
variavel = 1

for i in range(30):  # Número de repetições
    digitador = str(variavel)
    pgui.write(f"{digitador}")
    pgui.hotkey('space')
    print(f'Repetição nº [{i}] Pressionando a tecla: "space"...')
    time.sleep(1)
    pgui.hotkey('enter')
    print(f'Repetição nº [{i}] Pressionando a tecla: "enter"...')
    time.sleep(5)
    pgui.hotkey('alt', 'd')
    print(f'Repetição nº [{i}] Pressionando as teclas: "alt" + "d"...')
    pgui.write("https://www.bing.com/")
    print(f'Repetição nº [{i}] Digitando: "https://www.bing.com/"...')
    pgui.hotkey('enter')
    time.sleep(1)
    variavel += 1
