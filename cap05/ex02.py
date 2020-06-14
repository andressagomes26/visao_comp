'''
    * Capítulo 05: Pré-processamento

        5.1 Operações básicas
            > Acessando informações sobre a imagem
'''

import cv2
imagem = cv2.imread("frutas.jpeg")

print(imagem.shape) # Obter o número de linhas, colunas e canais de uma imagem
print(imagem.size)  # Obter  o  total  de  pixels  da  imagem,