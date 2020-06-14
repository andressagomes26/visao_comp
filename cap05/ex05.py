'''
    * Capítulo 05: Pré-processamento

        5.2  Histograma de Cores
            > Equalização de histograma
'''

import cv2
from matplotlib import pyplot as grafico

imagemOriginal = cv2.imread("maquina.jpg", 0)
imagemEqualizada = cv2.equalizeHist(imagemOriginal)

cv2.imshow("Imagem Original", imagemOriginal)
cv2.imshow("Imagem Equalizada", imagemEqualizada)

grafico.hist(imagemOriginal.ravel(), 256, [0,256])

grafico.figure();
grafico.hist(imagemEqualizada.ravel(), 256, [0,256])

grafico.show()

# Função equalizeHist = Equalizaa histogramas de imagen
# O resultado da execução:
    # Imagem original;
    # Imagem com o histogramae qualizado;
    # Gráficos referentes ao histograma de ambasas imagens.