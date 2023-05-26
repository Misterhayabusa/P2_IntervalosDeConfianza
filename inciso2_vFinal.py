import math
from scipy.stats import t, norm

def calcular_intervalo_confianza_diferencia_medias(media_muestra1, desviacion_estandar1, tamaño_muestra1, media_muestra2, desviacion_estandar2, tamaño_muestra2, nivel_confianza):
    if tamaño_muestra1 > 30 and tamaño_muestra2 > 30:
        # Utilizar distribución normal
        error_estandar = math.sqrt(  ((tamaño_muestra1) - 1)*((desviacion_estandar1)**2) + ((tamaño_muestra2) - 1)*((desviacion_estandar2)**2) / (tamaño_muestra1 + tamaño_muestra2 - 2) )
        #tabla
        numero= 1 - (1 - nivel_confianza) / 2
        alpha1= round(numero,3)
        valor_z = norm.ppf(alpha1)
        #formulazo
        formulazo=math.sqrt((1/tamaño_muestra1)+(1/tamaño_muestra2))
        margen_error = valor_z * error_estandar * formulazo
        distribucion = 'Normal'
    else:
        # Utilizar t de Student
        error_estandar = math.sqrt( ( (tamaño_muestra1 - 1)*(desviacion_estandar1**2) + (tamaño_muestra2 - 1)*(desviacion_estandar2**2)) / (tamaño_muestra1 + tamaño_muestra2 - 2) )
        #tabla
        numero = (1-nivel_confianza)/ 2
        alpha = round(numero, 3)
        fila=(tamaño_muestra1 + tamaño_muestra2 - 2)
        valor_t = t.ppf(1 - (1 - nivel_confianza) / 2, fila)
        #formulazo
        formulazo=math.sqrt((1/tamaño_muestra1)+(1/tamaño_muestra2))
        margen_error = valor_t * error_estandar * formulazo
        distribucion = 't de Student'
    intervalo_confianza = (media_muestra1 - media_muestra2 - margen_error, media_muestra1 - media_muestra2 + margen_error)
    return intervalo_confianza, distribucion

# Solicitar los datos al usuario
media_muestra1 = float(input("Ingrese la media de la primera muestra: "))
desviacion_estandar1 = float(input("Ingrese la desviación estándar de la primera población o de la primera muestra: "))
tamaño_muestra1 = int(input("Ingrese el tamaño de la primera muestra: "))
media_muestra2 = float(input("Ingrese la media de la segunda muestra: "))
desviacion_estandar2 = float(input("Ingrese la desviación estándar de la segunda población o de la segunda muestra: "))
tamaño_muestra2 = int(input("Ingrese el tamaño de la segunda muestra: "))
nivel_confianza = float(input("Ingrese el nivel de confianza deseado (entre 0 y 1): "))

# Calcular el intervalo de confianza y la distribución utilizada
intervalo, distribucion = calcular_intervalo_confianza_diferencia_medias(media_muestra1, desviacion_estandar1, tamaño_muestra1, media_muestra2, desviacion_estandar2, tamaño_muestra2, nivel_confianza)

# Imprimir el resultado
print(f"\nIntervalo de confianza para la diferencia de medias: {intervalo}")
print(f"Se utilizó la distribución: {distribucion}")
