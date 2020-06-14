'''
    * Capítulo 05: Pré-processamento

        5.4 Operações Aritméticas
            > Operação de mistura
'''


# Parâmetros da função addWeighted:
    # src1  =>  Matriz referente à primeira imagem = imagemFichasPretas;
    # alpha =>  Intensidade da primeira imagem = 0.2;
    # src2  =>  Matriz referente à segunda imagem = imagemFichasVermelhas;
    # beta  =>  Intensidade da segunda imagem = 1.0;
    # gamma =>  Valor escalar adicionado a cada soma = 0;

import cv2

imagemFichasVermelhas = cv2.imread("fichas-vermelhas.bmp")
imagemFichasPretas = cv2.imread("fichas-pretas.bmp")

imagem = cv2.addWeighted(imagemFichasPretas, 0.2, imagemFichasVermelhas, 1.0, 0)

cv2.imshow("Resultado", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()

