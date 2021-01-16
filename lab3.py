# -⁻- coding: UTF-8 -*-
simbolos = "0123456789abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ#$%&/\{}[]()-~_,.;:+-*'= °|¬áéíóúüÁÉÍÓÚÜ´âêîôûÂÊÎÔÛ^àèìòùÀÈÌÒÙ`¿?¡!<>@"
simbolos_dato = []
simbolos_valor = []
i = 0
while i < len(simbolos):
        simbolos_dato.append(simbolos[i])
        simbolos_valor.append(ord(simbolos[i]))
        i = i + 1
simbolos_dato.append('"')
simbolos_valor.append(ord('"'))

sim_dato_valor = [simbolos_dato,simbolos_valor]
sim_valor_ord = sorted(simbolos_valor)
for sim in sim_valor_ord:
        print(sim)
valor_maximo = max(sim_dato_valor[1]) + 1

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
        return XOR(c_binario_1,XOR(c_binario_2, llave))

def permutacion(c_binario_1, c_binario_2):
    nuevo_c_binario = c_binario_2 + c_binario_1
    return nuevo_c_binario

def cifrado_feistel(texto_binario, llave, t_bloque):
    i = 0
    t = len(texto_binario)
    cantidad = int(t/t_bloque)
    nuevo_texto_binario = texto_binario[0:t]
    while i < t:
        j = 0
        aux_texto_binario = ""
        while j <= cantidad*2:
            texto_binario_l = nuevo_texto_binario[j*int(t_bloque/2):(j+1)*int(t_bloque/2)]
            texto_binario_r = nuevo_texto_binario[(j+1)*int(t_bloque/2):(j+2)*int(t_bloque/2)]
            texto_binario_r_aux = sustitucion(texto_binario_l,texto_binario_r,llave)
            texto_binario_l_aux = texto_binario_r[0:len(texto_binario_r)]
            aux_texto_binario = aux_texto_binario + permutacion(texto_binario_r_aux, texto_binario_l_aux)
            j = j + 2
        nuevo_texto_binario = aux_texto_binario[0:t]
        i = i + 1
    return nuevo_texto_binario

def decifrado_feistel(texto_binario, llave, t_bloque):
    i = 0
    t = len(texto_binario)
    cantidad = int(t/t_bloque)
    nuevo_texto_binario = texto_binario[0:t]
    while i < t:
        j = 0
        aux_texto_binario = ""
        while j <= cantidad*2:
            texto_binario_l = nuevo_texto_binario[j*int(t_bloque/2):(j+1)*int(t_bloque/2)]
            texto_binario_r = nuevo_texto_binario[(j+1)*int(t_bloque/2):(j+2)*int(t_bloque/2)]
            texto_binario_l_aux = sustitucion(texto_binario_r,texto_binario_l,llave)
            texto_binario_r_aux = texto_binario_l[0:len(texto_binario_l)]
            aux_texto_binario = aux_texto_binario + permutacion(texto_binario_r_aux, texto_binario_l_aux)
            j = j + 2
        nuevo_texto_binario = aux_texto_binario[0:t]
        i = i + 1
    return nuevo_texto_binario

def texto_a_binario(texto):
        texto_binario = ""
        for simbolo in texto:
                texto_binario = texto_binario + dato_a_binario(simbolo)
        return texto_binario
#127
def binario_a_texto(texto_binario):
        texto = ""
        i = 0
        while i < int(len(texto_binario)/8):
                valor = binario_a_valor(texto_binario[i*8:(i+1)*8])
                if valor > 252:
                       valor = 32 + valor - 252
                if valor < 32:
                        valor = 252 - 32 + valor
                confirmar = 0
                simbolo = ""
                j = 0
                while j < len(sim_dato_valor[1]):
                        if valor == sim_dato_valor[1][j]:
                                confirmar = 1
                                simbolo = sim_dato_valor[0][j]
                                j = len(sim_dato_valor[1])
                        j = j + 1
                if confirmar == 0:
                        print("error")
                        simbolo = "#"
                texto = texto + simbolo
                i = i + 1
        return texto

texto = "Laboratio 3 - Sistemas de Comunicación"
texto_binario = texto_a_binario(texto)
texto_binario_encriptado = cifrado_feistel(texto_binario,"01010001",16)
texto_encriptado = binario_a_texto(texto_binario_encriptado)
print(texto_encriptado)
print(binario_a_texto(cifrado_feistel(texto_binario_encriptado,"01010001",16)))
