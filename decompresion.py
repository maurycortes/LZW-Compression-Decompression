from compresion import diccionario_inicial, salida

salida_decrypt = []
diccionario_reconstruido = {v: k for k, v in diccionario_inicial.items()}
cont = len(diccionario_reconstruido)

def lzw_decompresion():
    global cont
    codigo_viejo = salida[0]
    char = diccionario_reconstruido[codigo_viejo]
    salida_decrypt.append(char)
    for codigo in range(1, len(salida)):
        if salida[codigo] not in diccionario_reconstruido.keys():
            cadena = diccionario_reconstruido[codigo_viejo]
            cadena += char
        else:
            cadena = diccionario_reconstruido[salida[codigo]]
        salida_decrypt.append(cadena)
        char = cadena[0]
        diccionario_reconstruido[cont] = diccionario_reconstruido[codigo_viejo] + char
        cont += 1
        codigo_viejo = salida[codigo]
    result_string = ''.join(salida_decrypt)
    return result_string


resultado_decrypted = lzw_decompresion()
print("\nRESULTADO DECOMPRIMIDO")
print(resultado_decrypted)
