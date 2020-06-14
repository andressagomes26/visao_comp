'''
    * Capítulo 05: Pré-processamento

        5.3  Transformações Geométricas
            > Operação de translação
'''

#Função float32 = Gera a matriz de translação ou deslocamento;

# Resultado: A matriz de translação gerada desloca a imagem em
# 100  pixels  para  a  direita e em 100 pixels para baixo.

import cv2
import numpy as np

imagemOriginal = cv2.imread("folha.jpeg")
totalLinhas, totalColunas = imagemOriginal.shape[:2]

matriz = np.float32([[1, 0, 100], [0, 1, 100]])
imagemDeslocada = cv2.warpAffine(
    imagemOriginal,
    matriz,
    (totalColunas, totalLinhas)
)

cv2.imshow("Resultado", imagemDeslocada)

cv2.waitKey(0)
cv2.destroyAllWindows()

