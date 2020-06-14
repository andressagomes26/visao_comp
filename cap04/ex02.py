'''
    * Capítulo 04: Representação de cores no espaço

        4.1 Cores no espaço RGB
            > Combinando canais em uma imagem RGB
'''

import cv2

# Carregando imagem RGB e segmentando canais
imagem = cv2.imread("frutas.jpeg")
azul, verde, vermelho = cv2.split(imagem)

# Combinando os três canais em uma única imagem
imagem = cv2.merge((azul, verde, vermelho))
cv2.imshow("Resultado", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()