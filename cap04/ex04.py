'''
    * Capítulo 04: Representação de cores no espaço

        4.1 Cores no espaço HSV
            > Segmentando canais em uma imagem HSV
'''

import cv2

#Carregar imagem e transformar em escala de cinza
imagem = cv2.imread("frutas.jpeg")
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

#Segmentar em três canais no espaço HSV: split
matiz, saturacao, valor = cv2.split(imagem)

#Exibição de cada canal
cv2.imshow("Canal H", matiz)
cv2.imshow("Canal S", saturacao)
cv2.imshow("Canal V", valor)

cv2.waitKey(0)
cv2.destroyAllWindows()