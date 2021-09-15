#Ainda testando o envio para o Git
import pyautogui
import time

# 2 segundos de espera para cada linha de código
# pyautogui.PAUSE = 1.5

# Alterna abas antes de começar o código
pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')

for i in range(11):
    # 1 segundos de espera para começar o código
    #time.sleep(1)

    pyautogui.press('tab')

for i in range(36):
    pyautogui.press('0')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')

pyautogui.click(x=200, y=200)
time.sleep(1)
pyautogui.click(x=1100, y=640)
time.sleep(1)

pyautogui.scroll(-10)
pyautogui.press('tab')
time.sleep(1)

#pyautogui.write('Você não entregou a atividade!!! Entregue o mais urgente possível para não ficar sem nota.', interval=0.25) - Não aceitou caracteres especiais!!! Que pena!!!
pyautogui.keyDown('ctrl')
pyautogui.keyDown('v')
pyautogui.keyUp('v')
pyautogui.keyUp('ctrl')

pyautogui.click(x=1200, y=980)