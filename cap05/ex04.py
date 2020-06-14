'''
    * Capítulo 05: Pré-processamento

        5.2  Histograma de Cores
            > Histograma em uma imagem colorida
'''

import cv2
from matplotlib import pyplot as grafico

imagem = cv2.imread("folha-colorida.bmp")
azul, verde, vermelho = cv2.split(imagem)

grafico.hist(azul.ravel(), 256, [0,256])

grafico.figure()
grafico.hist(verde.ravel(), 256, [0,256])

grafico.figure()
grafico.hist(vermelho.ravel(), 256, [0,256])

grafico.show()

# Função  hist = Plotar cada histograma.
# Função  figure = Permite criar os três histogramas em apenas uma execução.