



'''
diccionario_inicial = {
    'C' : 0,
    'O' : 1,
    'M' : 2,
    'P' : 3,
    'A' : 4,
    'D' : 5,
    'R' : 6,
    'E' : 7,
    ' ' : 8,
    'N' : 9
}

diccionario = {
    'C' : 0,
    'O' : 1,
    'M' : 2,
    'P' : 3,
    'A' : 4,
    'D' : 5,
    'R' : 6,
    'E' : 7,
    ' ' : 8,
    'N' : 9
}

#cont = 10
'''


import math

diccionario = {}
cont = 0
salida = []
entrada = 'COMPADRE NO COMPRO COCO'


def llenar_diccionario_letras_iniciales():
    global cont
    unique_string = list(set(entrada))
    for char in unique_string:
        if char not in diccionario.keys():
            diccionario[char] = cont
            cont += 1
    return diccionario

def lzw_compresion():
    global cont
    w = ''
    for i in range(len(entrada)):
        k = entrada[i]
        wk = w + k

        if wk in diccionario.keys():
            w = wk
        else:
            salida.append(diccionario[w])
            diccionario[wk] = cont
            cont += 1
            w = k
    salida.append(diccionario[w])

def metricas():
    print("\n")
    print("DICCIONARIO")
    print(diccionario)
    print("SALIDA")
    print(salida)
    print("\n")
    repr_entrada = len(entrada) * 8 # cada caracter en ASCII * 8 bits
    log2_dict = math.ceil(math.log(len(diccionario), 2))
    repr_salida = len(salida) * log2_dict
    relacion_compresion = repr_entrada / repr_salida
    print("BITS UTILIZADOS EN LA ENTRADA")
    print(repr_entrada)
    print("BITS UTILIZADOS EN LA SALIDA")
    print(repr_salida)
    print("RELACION DE COMPRESION")
    print('{}:1'.format(round(relacion_compresion, 2)))





diccionario_inicial = llenar_diccionario_letras_iniciales()
lzw_compresion()
metricas()

