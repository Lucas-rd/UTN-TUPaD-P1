# NOTA: Para probar el codigo, descomentar el ejercicio que se desa probar quitando las comillas ''' '''

# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario
'''
def factorial_recursiva(num):
    if num == 0:
        return 1
    else:
        return num * factorial_recursiva(num - 1)

#Ingreso del numero por parte del usuario
numero = int(input("Ingrese el numero del que quiera calcular el factorial: "))

#Recorrida del factorial desde 1 hasta numero
for i in range(1, numero + 1):
    print(f"El factorial de { i } es { factorial_recursiva(i) }")
'''

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
'''
# fibonacci: 0 1 1 2 3 5 8 13
def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

numero = int(input("Ingrese el numero de posicion de fibonacci al que quiere llegar: "))

for i in range(numero):
    print(f"El numero de fibonacci en la posicion { i } es: { fibonacci_recursivo(i) }")
'''

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.
'''
def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero no negativo): "))

print(f"{base} elevado a la {exponente} es {potencia_recursiva(base, exponente)}")
'''

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.
'''
def decimal_a_binario(num):
    if num == 0:
        return '0'
    elif num == 1:
        return '1'
    else:
        return decimal_a_binario( num // 2) + str( num % 2 )

numero = int(input("Ingrese un numero para representar en binario: "))

if numero < 0:
    print("El numero ingresado debe ser positivo")
else:
    print(f"El numero { numero } ingresado equivale en binario a { decimal_a_binario(numero) }")
'''

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().
'''
def es_palindromo(palabra):
    longitud = len(palabra)

    if longitud <= 1:
        return True
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

palabra = input("Ingrese una palabra para evaluar si es palindromo: ").lower()

if " " in palabra:
    print("La palabra ingresada no es una palabra, contiene espacios")
else:
    print(es_palindromo(palabra))
'''

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)
'''
def suma_digitos(num):
    if num == 0:
        return 0
    else:
        return ( num % 10 ) + suma_digitos( num // 10 )

numero = int(input("Ingrese el numero que quiere sumar sus digitos: "))
print(suma_digitos(numero))
'''

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
'''
def contar_bloques(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return num + contar_bloques(num - 1)

cant_bloques = int(input("Ingrese la cantidad de bloques qu tendra la base de la piramide: "))

if cant_bloques < 0:
    print("Debe ingresar una cantidad positiva de bloques")
else:
    print(f"Para construir una piramide de {cant_bloques} bloques de base necesitara {contar_bloques(cant_bloques)} bloques")
'''

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
'''
def contar_digito(num, digito):
    if num == 0:
        return 0
    else:
        ultimo_numero = num % 10
        if ultimo_numero == digito:
            return 1 + contar_digito(num // 10, digito)
        else:
            return contar_digito(num // 10 , digito)

numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito del 0 al 9: "))

if numero < 0 or digito < 0 or digito > 9:
    print("Entrada no válida.")
else:
    print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el número {numero}.")
'''