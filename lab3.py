# -⁻- coding: UTF-8 -*-
# LABORATORIO 3 - SISTEMAS DE COMUNICACIÓN
# ESTUDIANTES: HUGO ARENAS
#              VICTOR HUANQUI
# DOCENTE: CARLOS GONZÁLEZ

from time import time

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

# ENTRADA: String 'texto', dígito 'llave' y dígito 'largo_bloque'.
# DESCRIPCIÓN: Encripta el 'texto'. Recorre el 'texto' cada 'largo_bloque' símbolos de este, diviéndose en 2 partes donde
#              la primera corresponde al fragmento_1 y la segunda al fragmento_2. Al fragmento_1 se le aplica una sustitución con
#              'llave'. Luego, se realiza la permutación entre el fragmento_1 sustituido y el fragmento_2 y el resultado es agregado
#              a un 'texto_aux'. Este proceso se repite una cantidad de veces igual al largo del 'texto'.
# SALIDA: Entrega el string 'texto_encriptado', correspondiente al último 'texto_aux' obtenido.
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

# ENTRADA: String 'texto_encriptado', dígito 'llave' y dígito 'largo_bloque'.
# DESCRIPCIÓN: Desencripta el 'texto_encriptado'. Recorre el 'texto' cada 'largo_bloque' símbolos de este, aplicándole una permutación
#              invertida entre su mitad izquierda y su mitad derecha. Luego, el fragmento permutado es dividido en 2 fragmentos del
#              mismo largo, fragmento_1 y fragmento_2. Finalmente, al 'texto_aux' se le agrega la sustitución invertida del fragmento_1
#              con 'llave' más el fragmento_2. Este proceso se repite una cantidad de veces igual al largo del 'texto_encriptado'.
# SALIDA: Entrega el string 'texto', correspondiente al último 'texto_aux' obtenido.
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

# ENTRADA: String 'cadena'.
# DESCRIPCIÓN: Transforma una cadena que contiene solo números en el digito respecto.
# SALIDA: Entrega el dígito respectivo de 'cadena'.
def cadena_a_digito(cadena):
        digito = 0
        for numero in cadena:
                digito = digito + int(numero)*pow(10,len(cadena) - cadena.index(numero) - 1)
        return digito

# ENTRADA: String 'llave_str'.
# DESCRIPCIÓN: Verifica que 'llave_str' cumpla las condiciones correctas. Si el largo de 'llave_str' es 0 o si algún símbolo no es
#              dígito, entonces se vuelve a ingresar por pantalla y se realiza la recursión con el nuevo 'llave_str'.
# SALIDA: Entrega 'llave_str' correcta transformada en un dígito.
def corroborar_llave(llave_str):
        if len(llave_str) == 0:
                print("Vuelva a ingresar un dígito.")
                llave_str = str(input("Ingrese llave numérica: "))
                return corroborar_llave(llave_str)
        elif any(llave_str.isdigit() for simbolo in llave_str) == False:
                print("Debe de ingresar un dígito.")
                llave_str = str(input("Ingrese llave numérica: "))
                return corroborar_llave(llave_str)
        else:
                return cadena_a_digito(llave_str)

# ENTRADA: String 'largo_bloque_str'.
# DESCRIPCIÓN: Verifica que 'largo_bloque_str' cumpla las condiciones correctas. Si el largo de 'largo_bloque_str' es 0 o si algún
#              símbolo no es dígito o si no es múltiplo de 16, entonces se vuelve a ingresar por pantalla y se realiza la recursión
#              con el nuevo 'largo_bloque_str'.
# SALIDA: Entrega 'largo_bloque_str' correcta transformada en un dígito.              
def corroborar_largo_bloque(largo_bloque_str):
        if len(largo_bloque_str) == 0:
                print("Vuelva a ingresar un dígito.")
                largo_bloque_str = str(input("Ingrese tamaño de bloque en bits(múltiplo de 16): "))
                return corroborar_largo_bloque(largo_bloque_str)
        elif any(largo_bloque_str.isdigit() for simbolo in largo_bloque_str) == False:
                print("Debe de ingresar un dígito.")
                largo_bloque_str = str(input("Ingrese tamaño de bloque en bits(múltiplo de 16): "))
                return corroborar_largo_bloque(largo_bloque_str)
        elif cadena_a_digito(largo_bloque_str)%16 != 0:
                print("El dígito no es múltiplo de 16.")
                largo_bloque_str = str(input("Ingrese tamaño de bloque en bits(múltiplo de 16): "))
                return corroborar_largo_bloque(largo_bloque_str)
        else:
                return cadena_a_digito(largo_bloque_str)
                

# Se ingresa por pantalla el texto plano para encriptar, corroborando que sea una entrada correcta y viendo si tiene un largo ideal.        
texto = str(input("Ingrese un texto o frase: "))
while len(texto) == 0:
        print("Debe ingresar un texto con un largo de al menos 1.")
        texto = str(input("Ingrese un texto o frase: "))
texto = largo_texto_ideal(texto)

# Se ingresa por pantalla la llave numérica de encriptación, corroborando que sea una entrada correcta. 
llave_str = str(input("Ingrese llave numérica: "))
llave = corroborar_llave(llave_str)

# Se ingresa por pantalla el largo de bloque, corroborando que sea una entrada correcta y viendo si tiene un largo ideal.
largo_bloque_str = str(input("Ingrese tamaño de bloque en bits(múltiplo de 16):"))
largo_bloque = int(corroborar_largo_bloque(largo_bloque_str)/8)
largo_bloque = largo_bloque_ideal(largo_bloque, largo_bloque, texto, 0)

# El 'texto' es encriptado, en base a un encriptador inspirado en el cifrado Feistel. Luego se imprime el texto cifrado.
te_i = time()
texto_encriptado = encriptacion(texto,llave,largo_bloque)
te_f = time()
te = te_f - te_i
throughput_e = largo_bloque/te
print(texto_encriptado)
print("Rendimiento de encriptación: " + str(throughput_e))

# El 'texto_encriptado' es desencriptado, en base a un desencriptador inspirado en el decifrado Feistel, lo vuelve a su largo original
# si es necesario y luego lo imprime.
td_i = time()
texto_desencriptado = desencriptacion(texto_encriptado,llave,largo_bloque)
if len(texto_desencriptado)%2 == 0 and texto_desencriptado[len(texto_desencriptado) - 1] == " ":
        texto_desencriptado = texto_desencriptado[0:len(texto_desencriptado) - 1]
td_f = time()
td = td_f - td_i
throughput_d = largo_bloque/td
print(texto_desencriptado)
print("Rendimiento de desencriptación: " + str(throughput_d))
