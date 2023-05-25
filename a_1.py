

import math
from scipy.stats import t

def calcular_intervalo_confianza(media_muestra, desviacion_estandar, tamaño_muestra, nivel_confianza):
    """
    Calcula el intervalo de confianza para la media poblacional.

    Parámetros:
    - media_muestra: la media de la muestra.
    - desviacion_estandar: la desviación estándar de la población (si se conoce) o de la muestra.
    - tamaño_muestra: el tamaño de la muestra.
    - nivel_confianza: el nivel de confianza deseado (entre 0 y 1).

    Devuelve:
    - intervalo_confianza: una tupla con los límites inferior y superior del intervalo de confianza.
    """
    error_estandar = desviacion_estandar / math.sqrt(tamaño_muestra)
    valor_t = t.ppf(1 - (1 - nivel_confianza) / 2, tamaño_muestra - 1)
    margen_error = valor_t * error_estandar
    intervalo_confianza = (media_muestra - margen_error, media_muestra + margen_error)
    return intervalo_confianza

# Solicitar los datos al usuario
media_muestra = float(input("Ingrese la media de la muestra: "))
desviacion_estandar = float(input("Ingrese la desviación estándar de la población o de la muestra: "))
tamaño_muestra = int(input("Ingrese el tamaño de la muestra: "))
nivel_confianza = float(input("Ingrese el nivel de confianza deseado (entre 0 y 1): "))

# Calcular el intervalo de confianza
intervalo = calcular_intervalo_confianza(media_muestra, desviacion_estandar, tamaño_muestra, nivel_confianza)

# Imprimir el resultado
print(f"\nIntervalo de confianza para la media: {intervalo}")