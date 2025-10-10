# 1 º Passo: Instalar o Pyautogui com comando:
# pip install pyautogui

# Crie uma automação que abra automaticamente um navegador

# Importamos a bibilioteca para o script em uso
import pyautogui

# 'Press' é um comando que utilizamos para pressionar a tecla desejada
pyautogui.press('Win') # para pressionar a tecla windows

# 'sleep' é um comando que utilizamos para deixar o código
# em espera por alguns segundos
pyautogui.sleep(1)

# 'Write' é um comando que utilizamos para passar o que queremos
# escrever
pyautogui.write('Google Chrome')

pyautogui.press('Enter')