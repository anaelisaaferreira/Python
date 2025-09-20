import pyautogui

pyautogui.press("win")
pyautogui.sleep(0.5)
pyautogui.write("Google Chrome",interval=0.1)
pyautogui.press("enter")
pyautogui.sleep(2)

pyautogui.click(871,589)
pyautogui.write ("https://prefeitura.santanadeparnaiba.sp.gov.br/Plataforma/smti/fabrica-de-programadores",interval=0.1)
pyautogui.press("enter")
pyautogui.sleep(1)

pyautogui.hotkey("printscreen")
pyautogui.mouseDown(0,0)
pyautogui.moveTo(1920,1080)
pyautogui.mouseUp()
