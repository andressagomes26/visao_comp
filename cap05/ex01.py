'''
    * Capítulo 05: Pré-processamento

        5.1 Operações básicas
            > Acessando e modificando valores de pixels
'''

import cv2
imagem = cv2.imread("frutas.jpeg")

# Para representar a cor de um pixel em uma imagem colorida
def ex1(imagem):
    valorPixel = imagem[150,150]
    print(valorPixel)


# Imagem em tons de cinza.
def ex2(imagem):
    imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)  #Converte a imagem RGB em tons de cinza
    valorPixel = imagem[150,150]
    print(valorPixel)


# Determinar o valor da intensidade da cor de um único canal
def ex3(imagem):
    valorPixel = imagem[150,150,0]
    print(valorPixel)


# Alterar o valor de um determinado pixel
def ex4(imagem):
    print(imagem[150,150])
    imagem[150,150] = [255,255,255]
    print(imagem[150,150])


ex1(imagem)
ex2(imagem)
ex3(imagem)
ex4(imagem)
