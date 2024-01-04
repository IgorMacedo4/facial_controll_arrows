import cv2
import mediapipe as mp
import pyautogui
from time import time

pyautogui.FAILSAFE = False

class NoseMouseController:
    def __init__(self, screen_width=1920, screen_height=1080, dead_zone=0.05):
        """Inicializa a captura de vídeo, a detecção de rosto e configura parâmetros de controle."""
        try:
            self.cam = cv2.VideoCapture(0)
            self.face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
            self.screen_width = screen_width
            self.screen_height = screen_height
            self.dead_zone = dead_zone
            self.last_press_time = time()
            self.press_delay = 0.5  # Delay entre pressionamentos de teclas
        except Exception as e:
            print(f"Erro na inicialização: {e}")

    def run(self):
        """Executa o loop principal para controle do mouse pelo nariz."""
        print("Posicione seu rosto no centro da tela e pressione 'c' para calibrar.")
        calibrated = False
        base_x, base_y = 0.5, 0.5  # Valores iniciais para calibração

        # Cria uma janela redimensionável
        cv2.namedWindow('Nose Mouse Controller', cv2.WINDOW_NORMAL)

        while True:
            try:
                _, frame = self.cam.read()
                frame = cv2.flip(frame, 1)  # Espelha o frame
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                output = self.face_mesh.process(rgb_frame)
                landmark_points = output.multi_face_landmarks

                if landmark_points:
                    landmarks = landmark_points[0].landmark
                    nose = landmarks[1]  # Ponta do nariz

                    # Converte coordenadas do nariz para pixels
                    nose_x = int(nose.x * frame.shape[1])
                    nose_y = int(nose.y * frame.shape[0])

                    # Calibração ao pressionar 'c'
                    if not calibrated and cv2.waitKey(1) & 0xFF == ord('c'):
                        base_x, base_y = nose.x, nose.y
                        calibrated = True
                        print("Calibrado com sucesso!")

                    # Controle de movimento após calibração
                    if calibrated:
                        dx = nose.x - base_x
                        dy = nose.y - base_y

                        current_time = time()
                        if current_time - self.last_press_time > self.press_delay:
                            # Envia comandos de pressionamento de teclas com base no movimento do nariz
                            if dx > self.dead_zone:
                                pyautogui.press('right')
                                self.last_press_time = current_time
                            elif dx < -self.dead_zone:
                                pyautogui.press('left')
                                self.last_press_time = current_time
                            
                            if dy > self.dead_zone:
                                pyautogui.press('down')
                                self.last_press_time = current_time
                            elif dy < -self.dead_zone:
                                pyautogui.press('up')
                                self.last_press_time = current_time

                    # Desenha um círculo na ponta do nariz para visualização
                    cv2.circle(frame, (nose_x, nose_y), 5, (0, 255, 0), -1)

                # Mostra o frame capturado
                cv2.imshow('Nose Mouse Controller', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            except Exception as e:
                print(f"Erro durante execução: {e}")
                break

        # Encerra a captura de vídeo e fecha todas as janelas
        cv2.destroyAllWindows()
        self.cam.release()

if __name__ == "__main__":
    try:
        screen_width, screen_height = pyautogui.size()
        nose_mouse_control = NoseMouseController(screen_width=screen_width, screen_height=screen_height)
        nose_mouse_control.run()
    except Exception as e:
        print(f"Erro ao iniciar o controlador: {e}")
