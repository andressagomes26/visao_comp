'''
    * Capítulo 04: Representação de cores no espaço

        4.1 Cores no espaço RGB
            > Segmentando Canais de uma imagem RGB
'''

import cv2

# Carregando imagem RGB e segmentando canais
imagem = cv2.imread("frutas.jpeg")          #Carregar a imagem: cv2.imread()
azul, verde, vermelho = cv2.split(imagem)   #Definição de  matrizes (azul, verde e vermelho): cvs.split()

# Exibindo imagens dos canais separados
cv2.imshow("Canal R", vermelho)             #Exibir canal de cor vermelho: cvs2.imshow()
cv2.imshow("Canal G", verde)                #Exibir canal de cor verde: cvs2.imshow()
cv2.imshow("Canal B", azul)                 #Exibir canal de cor azul: cvs2.imshow()

# Salvando imagens dos canais separados
cv2.imwrite("canal-vermelho.jpg", vermelho) #Salvar a imagem do canal vermelho: cv2.imwrite()
cv2.imwrite("canal-verde.jpg", verde)       #Salvar a imagem do canal verde: cv2.imwrite()
cv2.imwrite("canal-azul.jpg", azul)         #Salvar a imagem do canal azul: cv2.imwrite()

cv2.waitKey(0)
cv2.destroyAllWindows()