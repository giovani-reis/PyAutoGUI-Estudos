import pyautogui
import time

pyautogui.PAUSE = 0.6
#abriria o meu navegador (Chrome)
# pyautogui.press() -= apertar uma tecla
# pyayutogui.click - ckucar com o mouse
# pyautogui.write - escrever algo
# pyautogui.hotkey("crtl", "c") 

#entrar no hashtagtrienamentos.com/curso-python
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
pyautogui.hotkey("win", "up")
pyautogui.write("hashtagtreinamentos.com/curso-python")
pyautogui.press("enter")

time.sleep(2)
pyautogui.click(x=388, y=541)
pyautogui.scroll(-500)
pyautogui.click(x=947, y=641)
time.sleep(2.1)
pyautogui.scroll(-500)
pyautogui.click(x=935, y=825)

#preencher os formularios
pyautogui.click(x=811, y=467)
pyautogui.write("Giovani")
pyautogui.press("tab")
pyautogui.write("gi.giovani12929@gmail.com")
pyautogui.press("tab")
pyautogui.write("11")
pyautogui.press("tab")
pyautogui.write("192839993")

pyautogui.hotkey("alt", "f4")