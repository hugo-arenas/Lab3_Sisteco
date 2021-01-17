# -⁻- coding: UTF-8 -*-
simbolos = "0123456789abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ#$%&/\{}[]()-~_,.;:+*'= °|¬áéíóúüÁÉÍÓÚÜ´âêîôûÂÊÎÔÛ^àèìòùÀÈÌÒÙ`¿?¡!<>@"
simbolos_dato = []
simbolos_valor = []
i = 0
for s in simbolos:
        simbolos_dato.append(s)
        simbolos_valor.append(ord(s))
#while i < len(simbolos):
#        simbolos_dato.append(simbolos[i])
#        simbolos_valor.append(ord(simbolos[i]))
#        i = i + 1
simbolos_dato.append('"')
simbolos_valor.append(ord('"'))

def digito_a_binario(digito):
        binario = bin(digito)
        binario = binario[2:len(binario)]
        while len(binario) < 8:
                binario = "0" + binario
        return binario

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
  
def texto_a_binario(texto):
        texto_binario = ""
        for simbolo in texto:
                texto_binario = texto_binario + dato_a_binario(simbolo)
        return texto_binario

def largo_texto_ideal(texto):
        if len(texto)%2 != 0:
                return texto + " "
        else:
                return texto
def largo_bloque_ideal(largo_bloque, l_bloque, texto, direccion):
        if len(texto) < largo_bloque:
                return 0
        elif largo_bloque%2 == 1:
                return largo_bloque_ideal(largo_bloque + 1, l_bloque, texto, direccion)
        elif largo_bloque == 0:
                return 0
        elif len(texto)%largo_bloque == 0:
                return largo_bloque
        else:
                if direccion == 0:
                        b1 = largo_bloque_ideal(largo_bloque - 2, l_bloque, texto, -1)
                        b2 = largo_bloque_ideal(largo_bloque + 2, l_bloque, texto, 1)
                        if b1 == 0 and b2 != 0:
                                return b2
                        elif b1 != 0 and b2 == 0:
                                return b1
                        elif b1 == b2 and b1 == 0:
                                return 0
                        elif (l_bloque - b1) < (b2 - l_bloque):
                                return b1
                        else:
                                return b2
                elif direccion > 0:
                        return largo_bloque_ideal(largo_bloque + 2, l_bloque, texto, 1)
                else:
                        return largo_bloque_ideal(largo_bloque - 2, l_bloque, texto, -1)
        
def sustitucion(fragmento_texto, llave):
        fragmento_nuevo = ""
        for simbolo in fragmento_texto:
                posicion = simbolos_valor.index(ord(simbolo))
                posicion = (posicion + llave)%len(simbolos)
                fragmento_nuevo = fragmento_nuevo + simbolos_dato[posicion]
        return fragmento_nuevo

def sustitucion_inv(fragmento_texto, llave):
        fragmento_nuevo = ""
        for simbolo in fragmento_texto:
                posicion = simbolos_valor.index(ord(simbolo))
                indice = 0
                while (indice + llave)%len(simbolos) != posicion:
                        indice = indice + 1
                fragmento_nuevo = fragmento_nuevo + simbolos_dato[indice]
        return  fragmento_nuevo

def permutacion(fragmento_texto_1, fragmento_texto_2):
        fragmento_nuevo = ""
        i = 0
        while i < len(fragmento_texto_1):
                fragmento_nuevo = fragmento_nuevo + fragmento_texto_1[i] + fragmento_texto_2[len(fragmento_texto_2)-1-i]
                i = i + 1
        return fragmento_nuevo

def permutacion_inv(fragmento_texto_1, fragmento_texto_2):
        fragmento_aux = fragmento_texto_1 + fragmento_texto_2
        fragmento_1 = ""
        fragmento_2 = ""
        i = 0
        while i < len(fragmento_aux):
                fragmento_1 = fragmento_1 + fragmento_aux[i]
                fragmento_2 = fragmento_2 + fragmento_aux[len(fragmento_aux)-1-i]
                i = i + 2
        return fragmento_1 + fragmento_2

def encriptacion(texto, llave, largo_bloque):
        #texto = largo_texto_ideal(texto)
        #largo_bloque = largo_bloque_ideal(largo_bloque, texto)
        largo_t = len(texto)
        cantidad = int(largo_t/largo_bloque)
        texto_encriptado = texto[0:largo_t]
        i = 0
        while i < largo_t:
                j = 0
                texto_aux = ""
                while j <= cantidad*2:
                        fragmento_1 = texto_encriptado[j*int(largo_bloque/2):(j+1)*int(largo_bloque/2)]
                        fragmento_2 = texto_encriptado[(j+1)*int(largo_bloque/2):(j+2)*int(largo_bloque/2)]
                        fragmento_1 = sustitucion(fragmento_1, llave)
                        texto_aux = texto_aux + permutacion(fragmento_1, fragmento_2)
                        j = j + 2
                texto_encriptado = texto_aux[0:largo_t]
                i = i + 1
        return texto_encriptado

def desencriptacion(texto_encriptado, llave, largo_bloque):
        largo_t = len(texto_encriptado)
        cantidad = int(largo_t/largo_bloque)
        texto = texto_encriptado[0:largo_t]
        i = 0
        while i < largo_t:
                j = 0
                texto_aux = ""
                while j <= cantidad*2:
                        fragmento = texto[j*int(largo_bloque/2):(j+2)*int(largo_bloque/2)]
                        fragmento = permutacion_inv(fragmento[0:int(len(fragmento)/2)], fragmento[int(len(fragmento)/2):len(fragmento)])
                        fragmento_1 = fragmento[0:int(len(fragmento)/2)]
                        fragmento_2 = fragmento[int(len(fragmento)/2):len(fragmento)]
                        texto_aux = texto_aux + sustitucion_inv(fragmento_1, llave) + fragmento_2
                        j = j + 2
                texto = texto_aux[0:largo_t]
                i = i + 1
        if len(texto)%2 == 0 and texto[len(texto) - 1] == " ":
                return texto[0:len(texto) - 1]
        else:
                return texto

texto = "Laboratio 3 - Sistemas de Comunicación"
print(texto)
llave = 3
largo_bloque = int(48/8)
texto = largo_texto_ideal(texto)
largo_bloque = largo_bloque_ideal(largo_bloque, largo_bloque, texto, 0)
texto_encriptado = encriptacion(texto,llave,largo_bloque)
print(texto_encriptado)
texto_desencriptado = desencriptacion(texto_encriptado,llave,largo_bloque)
print(texto_desencriptado)
