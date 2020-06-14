'''
    * Capítulo 03: Aquisição de Imagem

        3.7 Práticas com Python e OpenCV
            > Carregando imagens a partir de arquivos
'''

# Carregando imagens a partir de arquivos

import cv2

imagem = cv2.imread("imagem.jpg")
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()