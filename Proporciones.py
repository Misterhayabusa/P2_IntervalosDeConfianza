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

T99=[0,63.656,9.925,5.841,4.604,4.032,3.707,3.499,3.355,3.250,3.169,3.106,3.055,3.012,2.977,2.947,2.921,2.898,2.878,2.861,2.845,2.831,2.819,2.807,2.797,2.787,2.779,2.771,2.763,2.756,2.750]
T95=[0,12.706,4.303,3.182,2.776,2.571,2.447,2.365,2.306,2.262,2.228,2.201,2.201,2.179,2.160,2.145,2.131,2.120,2.110,2.101,2.093,2.086,2.080,2.074,2.069,2.064,2.060,2.056,2.052,2.048,2.045]
T90=[0,6.314,2.920,2.353,2.132,2.015,1.943,1.895,1.860,1.833,1.812,1.796,1.782,1.771,1.761,1.753,1.746,1.740,1.734,1.729,1.725,1.721,1.717,1.714,1.711,1.708,1.706,1.703,1.701,1.699,1.697]

def IC_DifProp(NC, p1, n1, p2, n2):
    if n1>=30:
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
    else:
        if NC == 90:
            NC = T90[n1]
        elif NC == 95:
            NC = T95[n1];
        elif NC == 99:
            NC = T99[n1];
        else:
            print('Nivel de confianza no valido')

    p_1=p1/n1
    p_2=p2/n2

    Inter1 = round(((p_1 - p_2)-NC*(math.sqrt((p_1*(1-p_1)/n1)+(p_2*(1 - p_2)/n2)))), 3)
    Inter2= round(((p_1 - p_2)+NC*(math.sqrt((p_1*(1-p_1)/n1)+(p_2*(1-p_2)/n2)))), 3)

    print(f'[{Inter1}<=p1 - p2>={Inter2}]')


def IC_Prop(NC, p1, n):
    if n>=30:
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
    else:
        if NC == 90:
            NC = T90[n];
        elif NC == 95:
            NC = T95[n];
        elif NC == 99:
            NC = T99[n];
        else:
            print('Nivel de confianza no valido')

    p_1=p1/n

    Inter1 = round((p_1-NC*(math.sqrt((p_1*(1-p_1)/n)))), 3)
    Inter2 = round((p_1+NC*(math.sqrt((p_1*(1-p_1)/n)))), 3)

    print(f'[{Inter1}<=p1>={Inter2}]')


IC_DifProp(98, 12, 50, 12, 60)
