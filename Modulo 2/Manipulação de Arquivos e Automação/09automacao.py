# Desenhar um objeto 
# após a execução do código abra um bloco de notas para o desenho ser criado.

import pyautogui
import time

pyautogui.press("win")
time.sleep(1)
pyautogui.write("Bloco de Notas")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("Desenhando com Pyautogui")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)

arvore = [
    "    ^    ", # 4 espaços para cada lado
    "   ^^^  ", # 3 espaços para cada lado
    "  ^^^^^ ", # 2 espaços para cada lado
    "   |||   ", # 3 espaços para cada lado
    "   |||   ",
]

for linha in arvore:
    pyautogui.write(linha, interval=0.1)
    pyautogui.press("enter")
pyautogui.write("Desenho finalizado!")
print("Desenho da árvore concluído!")
 