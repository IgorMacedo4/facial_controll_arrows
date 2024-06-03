# FacialControllArrows

## Descrição
FacialControllArrows é um que permite controlar o cursor do mouse usando os movimentos do nariz, capturados por uma webcam. Utilizando a tecnologia de visão computacional através das bibliotecas OpenCV e MediaPipe, este projeto mapeia os movimentos do nariz e os converte em comandos de controle de cursor, proporcionando uma maneira única e interativa de interagir com sua interface de usuário.

## Funcionalidades
- Detecção em tempo real do movimento do nariz usando a webcam.
- Conversão de movimentos do nariz em comandos de controle do cursor.
- Calibração simples e intuitiva para começar.
- Interface redimensionável para visualizar o controle em ação.

## Calibração
A calibração é um passo essencial para garantir a precisão e a eficácia do controle do mouse. Siga estes passos para calibrar o sistema:

1. Posicione seu rosto no centro da tela.
2. Olhe diretamente para a webcam.
3. Pressione a tecla 'c' para calibrar o sistema.

Após a calibração, o sistema capturará a posição inicial do nariz e a usará como referência para todos os movimentos futuros. Movimentos relativos a este ponto central são usados para controlar o cursor.

## Como Usar
1. Clone o repositório para sua máquina local.
2. Certifique-se de ter todas as dependências instaladas (listadas em `requirements.txt`).
3. Execute o script principal para iniciar o programa.
4. Siga as instruções na tela para calibrar e começar a usar.

## Dependências
- OpenCV
- MediaPipe
- PyAutoGUI

## Autor
- Igor Macedo(https://github.com/IgorMacedo4)
