'''
    * Capítulo 05: Pré-processamento

        5.3  Transformações Geométricas
            > Ajuste de escala
'''

# Parâmetros:
    # fx: Fator de escala horizontal;
    # fy: Fator de escala vertical.
    # cv2.INTER_CUBIC: Interpolação

import cv2

imagemOriginal = cv2.imread("folha.jpeg")

imagemModificada = cv2.resize(
    imagemOriginal, None, fx = 0.5, fy = 0.5,
    interpolation = cv2.INTER_CUBIC
)

cv2.imshow("Resultado", imagemModificada)

cv2.waitKey(0)
cv2.destroyAllWindows()
