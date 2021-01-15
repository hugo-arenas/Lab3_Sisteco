# -⁻- coding: UTF-8 -*-
simbolos = "0123456789abcdefghijklmnñopqrstuvwxyABCDEFGHIJKLMNÑOPQRSTUVWXYZ#$%&/\{}[]()-_,.;:+-*'= °|¬áéíóúüÁÉÍÓÚÜ´âêîôûÂÊÎÔÛ^àèìòùÀÈÌÒÙ`¿?¡!"
print(simbolos)
simbolos_dato = []
simbolos_valor = []
i = 0
while i < len(simbolos):
        simbolos_dato.append(simbolos[i])
        simbolos_valor.append(ord(simbolos[i]))
        print(ord(simbolos[i]))
        i = i + 1
simbolos_dato.append('"')
simbolos_valor.append(ord('"'))

sim_dato_valor = [simbolos_dato,simbolos_valor]

def binario_a_valor(cadena_binaria):
    digito = 0
    i = 0
    while i < len(cadena_binaria):
        if cadena_binaria[len(cadena_binaria)-i-1]=="1":
            digito = digito + pow(2,i)
        i = i + 1
    return digito

def dato_a_binario(dato):
        binario = str(bin(ord(dato)))
        if len(binario) == 10:
                return binario[2:len(binario)]
        else:
                i = len(binario)-2
                aux_binario = binario[2:len(binario)]
                while i < 8:
                        aux_binario = "0" + aux_binario
                        i = i + 1
                return aux_binario
                
        
def compuesto_binario(cadena_binaria):
    nuevo_frag = ""
    for binario in c_binario:
        if binario == "1":
            nuevo_frag = nuevo_frag + "0"
        if binario == "0":
            nuevo_frag = nuevo_frag + "1"
    return nuevo_frag


def XOR(c_binario_1, c_binario_2):
    nuevo_frag = ""
    i = 0
    while i < len(c_binario_1):
        if c_binario_1[len(c_binario_1)-i-1] != c_binario_2[len(c_binario_2)-i-1]:
            nuevo_frag = "1" + nuevo_frag
        else:
            nuevo_frag = "0" + nuevo_frag
        i = i + 1
    return nuevo_frag

def sustitucion(c_binario_1, c_binario_2, llave):
        return XOR(c_binario_1,XOR(_binario_2, llave))

def permutacion(c_binario_1, c_binario_2):
    nuevo_c_binario = c_binario_2 + c_binario_1
    return nuevo_c_binario

def cifrado_feistel(texto_binario, llave, t_bloque):
    i = 0
    t = len(texto_binario)
    t_c_binario = int(t/t_bloque)
    nuevo_texto_binario = texto_binario[0:t]
    while i < t:
        j = 0
        aux_texto_binario = ""
        while j < t_c_binario*2:
            texto_binario_l = nuevo_texto_binario[j*int(t/(t_c_binario*2)):(j+1)*int(t/(t_c_binario*2))]
            texto_binario_r = nuevo_texto_binario[(j+1)*int(t/(t_c_binario*2)):(j+2)*int(t/(t_c_binario*2))]
            texto_binario_r_aux = sustitucion(texto_binario_r,texto_binario_l,llave)
            aux_texto_binario = aux_texto_binario + permutacion(texto_binario_l, texto_binario_r_aux)
            j = j + 2
        nuevo_texto_binario = aux_texto_binario[0:t]
        i = i + 1
    return nuevo_texto_binario
