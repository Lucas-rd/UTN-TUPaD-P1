# NOTA: Para probar el codigo, descomentar el ejercicio que se desa probar quitando las comillas ''' '''

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
# Para este ejercicio usare un for ya que conozco la cantidad exacta de iteraciones que necesito. Podria hacerlo con in While pero es mas ineficiente porque tendria que decalrar una variable mas para el contador
'''
for i in range(0, 101, 1):
    print(i)
'''

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
# Para este ejercicio usamos la 'division entera' // la cual nos permite quitarle el ultimo digito al numero ingresado para asi poder contarlos con una variable contadora. Como no conocemos el largo del digito antes de iniciar el ciclo debemos usar una estructura while
'''
num = int(input("Ingrese un numero entero: "))
cont = 0

if num == 0:
    print("El numero tiene un solo digito y es el 0")
else:
    while num > 0:
        num = num // 10
        cont += 1
    print(f"El numero ingresado tiene { cont } digitos")
'''

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
'''
num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
acum = 0

if num1 > num2:
    i = num2
    # codigo caso num1 es mayor que num2
    for i in range( num2 + 1, num1, 1 ):
        acum += i
    print(f"La suma de todos los numeros comprendidos entre {num1} y {num2} excluyendo a ellos es: {acum}")        
elif num1 < num2:
    # codigo caso num2 es mayor que num1
    i = num1
    for i in range( num1 + 1, num2, 1 ):
        acum += i
    print(f"La suma de todos los numeros comprendidos entre {num1} y {num2} excluyendo a ellos es: {acum}")
else:
    # codigo caso iguales
    print("La suma da 0 porque ambos numeros son iguales")
'''


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
'''
acum = 0
num = int(input("Ingrese un numero (con '0' interrumpe la ejecucion): "))

while num != 0:
    acum += num
    num = int(input("Ingrese otro numero (con '0' interrumpe la ejecucion): "))

print(f"La suma de todos los numeros ingresados es: {acum}")
'''

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
'''
# Importamos random de Python para la generacion del numero aleatorio
import random

aleatorio = random.randint(0, 9)
num = int(input("Ingrese un numero para adivinar: "))
acum_intentos = 1

while num != aleatorio:
    acum_intentos += 1
    num = int(input("Incorrecto! Intente con otro numero para adivinar: "))

print(f"Usted necesito {acum_intentos} intentos")
'''

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
'''
for i in range(100, -1, -1):
    print(i)
'''

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
'''
num = int(input("Ingrese un numero: "))
acum = 0
if num >= 0:
    for i in range(0, num + 1):
        acum += i

    print(f"La suma desde 0 hasta {num} es: {acum}")
else:
    print("Error, el numero ingresado debe ser entero y positivo")
'''

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
'''
cantidad_numeros = 100 #Esta es la variable que me permitira ajustar el programa para recibir N numeros.
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(0, cantidad_numeros):
    num = int(input("Ingrese un numero: "))
    if num > 0:
        positivos += 1
    else:
        negativos += 1
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Se ingresaron {cantidad_numeros} numero/s. Dentro de esos {pares} eran pares, {impares} eran impares, y teniamos {positivos} valores positivos y {negativos} valores negativos.")
'''

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
'''
cantidad_numeros = 100 #Esta es la variable que me permitira ajustar el programa para recibir N numeros.
acum = 0

for i in range(0, cantidad_numeros):
    num = int(input("Ingrese un numero: "))
    acum += num

media = acum / cantidad_numeros

print(f"La media de los {cantidad_numeros} numeros ingresados es: {media}")
'''

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
'''
num = int(input("Ingrese un numero: "))
abs_num = abs(num) #Opte por hacerlo con absoluto para evitar errores con elos negativos.
num_inv = ''

while abs_num > 0:
    num_inv = str(num_inv) + str(abs_num % 10)
    abs_num = abs_num // 10

print(f"El numero inverso a {num} es: {num_inv}")
'''