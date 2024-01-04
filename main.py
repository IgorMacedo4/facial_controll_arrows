# Imports necessários
from controlArrows import NoseMouseController
import pyautogui

# Verifica se o script é o ponto de entrada principal
if __name__ == "__main__":
    try:
        # Obtém as dimensões da tela usando pyautogui
        screen_width, screen_height = pyautogui.size()
        # Cria uma instância da classe NoseMouseController com as dimensões da tela
        nose_mouse_control = NoseMouseController(screen_width=screen_width, screen_height=screen_height)
        # Inicia a execução do controlador do mouse pelo nariz
        nose_mouse_control.run()
    except Exception as e:
        # Captura e imprime qualquer exceção que ocorra durante a inicialização e execução
        print(f"Erro ao iniciar o controlador: {e}")
