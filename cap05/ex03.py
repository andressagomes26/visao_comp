'''
    * Capítulo 05: Pré-processamento

        5.2  Histograma de Cores
            > Histograma em uma imagem binária
'''

import cv2
from matplotlib import pyplot as grafico

imagem = cv2.imread("folha-binaria.bmp", 0)
grafico.hist(imagem.ravel(), 256, [0,256])
grafico.show()

# Função hist = ilustra  o  histograma  de  cores  da  imagem
# Método ravel =  transforma a imagem em um vetor