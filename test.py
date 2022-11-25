import numpy as np

c1_2 = [
    [200, 160, 120],
    [210, 170, 130],
    [215, 172, 133],
    [210, 165, 134],
    [198, 177, 138]
]


def media(clase):
    media = [0, 0, 0]

    for i in clase:
        for j in range(len(i)):
            media[j] += i[j]

    for i in range(len(media)):
        media[i] /= len(clase)

    return media


patron = [37, 150, 190]
c1_2 = np.array(c1_2)
valor_media = media(c1_2)
covarianza = np.cov(c1_2.T)
media = np.transpose(valor_media)[np.newaxis]
final = np.subtract(patron, media)
print(covarianza, final)
distancia = final @ np.linalg.inv(covarianza) @ final.T
print(distancia)
