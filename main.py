# main.py
import pyautogui
from control_arrows import NoseMouseController  # Ajuste o import conforme o nome do seu arquivo

def main():
    try:
        # Captura as dimensões da tela para configurar a classe NoseMouseController
        screen_width, screen_height = pyautogui.size()
        
        # Instancia a classe com as dimensões capturadas
        controller = NoseMouseController(screen_width=screen_width, screen_height=screen_height)
        
        # Inicia o controlador de mouse
        controller.run()
    except Exception as e:
        print(f"Erro ao iniciar o controlador de mouse pelo nariz: {e}")

if __name__ == "__main__":
    main()
