# Crie uma automação que escreva um texto automaticamente 

import pyautogui
import time

# Observação: Abra um bloco de notas vazio
# Aguarde 5 segundos para você abru o bloco de notas
time.sleep(5)

# Escreva o texto
pyautogui.write('Automatizando com Pyautogui', interval=0.1)