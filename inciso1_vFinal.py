import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, norm

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
    if tamaño_muestra > 30:
        error_estandar = desviacion_estandar / math.sqrt(tamaño_muestra)
        valor_z = norm.ppf(1 - (1 - nivel_confianza) / 2)
        margen_error = valor_z * error_estandar
    else:
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
calcular_cola_inferior = input("¿Desea calcular y graficar la cola inferior? (s/n): ")
calcular_cola_superior = input("¿Desea calcular y graficar la cola superior? (s/n): ")

# Calcular el intervalo de confianza
intervalo = calcular_intervalo_confianza(media_muestra, desviacion_estandar, tamaño_muestra, nivel_confianza)
print(f"\nIntervalo de confianza para la media: {intervalo}")

# Crear datos para la gráfica
x = np.linspace(intervalo[0] - 10, intervalo[1] + 10, 100)

if tamaño_muestra > 30:
    y = norm.pdf(x, media_muestra, desviacion_estandar / np.sqrt(tamaño_muestra))
else:
    y = t.pdf(x, tamaño_muestra - 1, media_muestra, desviacion_estandar / math.sqrt(tamaño_muestra))

# Generar la gráfica
plt.plot(x, y, 'b-', label='Distribución')
plt.fill_between(x, y, where=(x >= intervalo[0]) & (x <= intervalo[1]), color='gray', alpha=0.5, label='Intervalo de Confianza')
plt.axvline(x=media_muestra, color='r', linestyle='--', label='Media de la Muestra')

if calcular_cola_inferior.lower() == 's':
    if tamaño_muestra > 30:
        y_cola_inferior = norm.pdf(x, media_muestra, desviacion_estandar / np.sqrt(tamaño_muestra)) * (x < intervalo[0])
    else:
        y_cola_inferior = t.pdf(x, tamaño_muestra - 1, media_muestra, desviacion_estandar / math.sqrt(tamaño_muestra)) * (x < intervalo[0])
    plt.fill_between(x, y_cola_inferior, color='red', alpha=0.5, label='Cola Inferior')

if calcular_cola_superior.lower() == 's':
    if tamaño_muestra > 30:
        y_cola_superior = norm.pdf(x, media_muestra, desviacion_estandar / np.sqrt(tamaño_muestra)) * (x > intervalo[1])
    else:
        y_cola_superior = t.pdf(x, tamaño_muestra - 1, media_muestra, desviacion_estandar / math.sqrt(tamaño_muestra)) * (x > intervalo[1])
    plt.fill_between(x, y_cola_superior, color='blue', alpha=0.5, label='Cola Superior')

plt.legend()
plt.xlabel('Valores')
plt.ylabel('Densidad de Probabilidad')
plt.title('Intervalo de Confianza para la Media')
plt.grid(True)

# Mostrar la gráfica
plt.show()
