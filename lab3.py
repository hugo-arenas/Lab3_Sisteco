# -⁻- coding: UTF-8 -*-
# LABORATORIO 3 - SISTEMAS DE COMUNICACIÓN
# ESTUDIANTES: HUGO ARENAS
#              VICTOR HUANQUI
# DOCENTE: CARLOS GONZÁLEZ

# Tras definir un string con todos los símbolos conocidos posibles en español, se define un arreglo vacio para guardar por separado
# los símbolos del string 'simbolos'.
simbolos = "0123456789abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ#$%&/\{}[]()-~_,.;:+*'= °|¬áéíóúüÁÉÍÓÚÜ´âêîôûÂÊÎÔÛ^àèìòùÀÈÌÒÙ`¿?¡!<>@"
simbolos_dato = []

# Se guarda cada símbolo en el arreglo 'simbolos_dato'
for s in simbolos:
        simbolos_dato.append(s)

# Se agrega el símbolo '"' en el arreglo 'simbolos_dato', dejando este arreglo como un dato global.     
simbolos_dato.append('"')

# ENTRADA: String 'texto'.
# DESCRIPCIÓN: Agrega un espacio al final del string 'texto' si este posee un largo impar.
# SALIDA: Entrega el string 'texto' tanto si se le agrego el espacio al final como no.
def largo_texto_ideal(texto):
        if len(texto)%2 != 0:
                return texto + " "
        else:
                return texto

# ENTRADA: Dígito 'largo_bloque', dígito 'l_bloque', string 'texto' y dígito 'direccion'.
# DESCRIPCIÓN: Busca un 'largo_bloque' ajustado para el 'texto'. Inicialmente, 'largo_bloque' es igual a 'l_bloque' y
#              y 'direccion' es igual a 0. Si 'largo_bloque' es mayor a largo de 'texto' y 'direccion' es distinto
#              de 0, entonces retorna 0. Si 'largo_bloque' es impar, entonces se hace recursión aumentando
#              'largo_bloque' y 'l_bloque' en 1. Si 'largo_bloque' es 0, entonces retorna 0. Si el módulo entre el
#              largo de 'texto' y 'largo_bloque' es 0, entonces se retorna 'largo_bloque' pues ya es el ideal. Sino,
#              entonces puede suceder 3 cosas:
#              (1) Si 'direccion' es 0, entonces se crean 2 variables: b1=largo_bloque_ideal(largo_bloque-2,l_bloque,texto,-1)
#                  y b2=largo_bloque_ideal(largo_bloque+2,l_bloque,texto,1). Obteniendo sus resultados, si uno de ellos es 0
#                  y el otro no, entonces se retorna aquella variable que no de 0. Sino, si b1 y b2 son 0, entonces se retorna
#                  0. Sino, si 'l_bloque' menos b1 es menor a b2 menos 'l_bloque', entonces se retorna b1. Si no se cumple este
#                  último, entonces se retorna b2.
#              (2) Sino, si 'direccion' es mayor a 0 (o solo valor 1), entonces retorna la recursión de la función, aumentando
#                  en 2 el 'largo_bloque' y dejando 'direccion' como 1.
#              (3) Sino, si 'direccion' es menor a 0 (o solo valor -1), entonces retorna la recursión de la función, disminuyendo
#                  en 2 el 'largo_bloque' y dejando 'direccion' como -1.
# SALIDA: Entrega el 'largo_bloque' ideal.
def largo_bloque_ideal(largo_bloque, l_bloque, texto, direccion):
        if len(texto) < largo_bloque and direccion != 0:
                return 0
        elif largo_bloque%2 == 1:
                return largo_bloque_ideal(largo_bloque + 1, l_bloque + 1, texto, direccion)
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

# ENTRADA: String 'fragmento_texto' y dígito 'llave'.
# DESCRIPCIÓN: Crear un string 'fragmento_nuevo', agregando a el cada símbolo reemplazado del 'fragmento_texto' hacia 'llave'
#              posiciones a la derecha, considerando en todo momento que se hace módulo respecto al largo de 'simbolos_dato'.
# SALIDA: Entrega el string 'fragmento_nuevo'.       
def sustitucion(fragmento_texto, llave):
        fragmento_nuevo = ""
        for simbolo in fragmento_texto:
                posicion = simbolos_dato.index(simbolo)
                posicion = (posicion + llave)%len(simbolos_dato)
                fragmento_nuevo = fragmento_nuevo + simbolos_dato[posicion]
        return fragmento_nuevo

# ENTRADA: String 'fragmento_texto' y dígito 'llave'.
# DESCRIPCIÓN: Crear un string 'fragmento_nuevo'. Recorre cada símbolo de 'fragmento_texto' y busca su posición dentro de
#              'simbolos_dato'. Luego, realiza un ciclo buscando un índice que al ser sumado con la 'llave' y modulado por
#              el largo de 'simbolos_dato', de como resultado la posición del símbolo en 'simbolos_dato'. Un vez obtenido el
#              índice, a 'fragmento_nuevo' se le agrega el símbolo ubicado en la posición 'indice' dentro de 'simbolos_dato'.
# SALIDA: Entrega el string 'fragmento_nuevo'.
def sustitucion_inv(fragmento_texto, llave):
        fragmento_nuevo = ""
        for simbolo in fragmento_texto:
                posicion = simbolos_dato.index(simbolo)
                indice = 0
                while (indice + llave)%len(simbolos_dato) != posicion:
                        indice = indice + 1
                fragmento_nuevo = fragmento_nuevo + simbolos_dato[indice]
        return  fragmento_nuevo

# ENTRADA: String 'fragmento_texto_1' y string 'fragmento_texto_2'.
# DESCRIPCIÓN: Crear un string 'fragmento_nuevo' vacío. Se le va agregando simultáneamente cada símbolo de 'fragmento_texto_1'
#              y 'fragmento_texto_2', el primero desde la posición inicial hasta la final y el segundo desde la posición final
#              hacia la inicial.
# SALIDA: Entrega el string 'fragmento_nuevo'.
def permutacion(fragmento_texto_1, fragmento_texto_2):
        fragmento_nuevo = ""
        i = 0
        while i < len(fragmento_texto_1):
                fragmento_nuevo = fragmento_nuevo + fragmento_texto_1[i] + fragmento_texto_2[len(fragmento_texto_2)-1-i]
                i = i + 1
        return fragmento_nuevo

# ENTRADA: String 'fragmento_texto_1' y string 'fragmento_texto_2'.
# DESCRIPCIÓN: Crear un string 'fragmento_nuevo' vacío. Se le va agregando simultáneamente cada símbolo de 'fragmento_texto_1'
#              y 'fragmento_texto_2', el primero desde la posición inicial hacia 2 saltos de posición a la derecha y el segundo
#              desde la posición final hacia 2 saltos de posición a la izquierda.
# SALIDA: Entrega el string 'fragmento_nuevo'.
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
