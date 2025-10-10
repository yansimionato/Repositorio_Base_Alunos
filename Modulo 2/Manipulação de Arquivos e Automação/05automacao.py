import pyautogui
import webbrowser
import time

# Passo 1: Abrir o YouTube com uma música específica
url = 'https://www.youtube.com/watch?v=4InSuadZzIU'
webbrowser.open(url)

# Passo 2: Aguardar o carregamento da página
time.sleep(5) # ajustar de acordo com a velocidade da internet utilizada

# Passo 3 : Garantir que o vídeo comece (aperte o espaço para "play")
pyautogui.press('space') # toca ou pausa o vídeo