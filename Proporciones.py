import math

'''
3. IC para la proporción
4. IC diferencia de proporciones

Intervalos de confianza del 90, 95 y 99%
'''
Z90=1.65;
Z95=1.95; 

Z98=2.32;
Z99=2.58;

def IC_DifProp(NC, p1, n1, p2, n2):
    if NC == 90:
        NC = Z90;
    elif NC == 95:
        NC = Z95;
    elif NC == 98:
        NC = Z98;
    elif NC == 99:
        NC = Z99;
    else:
        print('Nivel de confianza no valido')

    p_1=p1/n1
    p_2=p2/n2

    Inter1 = round(((p_1 - p_2)-NC*(math.sqrt((p_1*(1-p_1)/n1)+(p_2*(1 - p_2)/n2)))), 3)
    Inter2= round(((p_1 - p_2)+NC*(math.sqrt((p_1*(1-p_1)/n1)+(p_2*(1-p_2)/n2)))), 3)

    print(f'[{Inter1}<=p1 - p2>={Inter2}]')


def IC_Prop(NC, p1, n):
    if NC == 90:
        NC = Z90;
    elif NC == 95:
        NC = Z95;
    elif NC == 98:
        NC = Z98;
    elif NC == 99:
        NC = Z99;
    else:
        print('Nivel de confianza no valido')


    p_1=p1/n

    Inter1 = round((p_1-NC*(math.sqrt((p_1*(1-p_1)/n)))), 3)
    Inter2 = round((p_1+NC*(math.sqrt((p_1*(1-p_1)/n)))), 3)

    print(f'[{Inter1}<=p1>={Inter2}]')


IC_DifProp(98, 12, 50, 12, 60)
