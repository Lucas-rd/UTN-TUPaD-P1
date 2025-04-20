# NOTA: Para probar el codigo, descomentar el ejercicio que se desa probar quitando las comillas ''' '''


# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
'''
#Definicion de funciones:
def impresion_de_cadena(cadena):
    print(cadena)

def imprimir_hola_mundo():
    print('Hola Mundo!')

# Programa principal:
imprimir_hola_mundo()
'''

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.
'''
#Definicion de funciones:
def saludar_usuario(usuario):
    print(f'Hola {usuario}!')

# Programa principal:
user= input("Ingrese su nombre: ")
saludar_usuario(user)
'''

# 3. Crear una función llamada informacion_personal(nombre, apellido,edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
'''
#Definicion de funciones:
def informacion_personal(nombre, apellido, edad, residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

# Programa principal:
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)
'''

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
'''
#Definicion de funciones:
import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    print(f'El area de un circulo para el radio ingresado es: {area}')

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f'El perimetro de un circulo para el radio ingresado es: {perimetro}')

radio = int(input("Ingrese el radio de un circulo en cm: "))

# Programa principal:
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)
'''

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
'''
#Definicion de funciones:
def segundos_a_horas(seg):
    # Podria haber resuelto todo aqui devolviendo un print en lugar de hacer un return de la variable pero lo hice asi para practicar retornar valores.
    return seg / 3600

def informar_horas(seg):
    horas = segundos_a_horas(seg)
    print(f"Los segundos ingresados equivalen a {horas} horas")

# Programa principal
segundos = int(input("Ingrese los segundos que desa convertir: "))
informar_horas(segundos)
'''


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.
'''
#Definicion de funciones:

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal:
numero = int(input("Ingrese un numero para calcular su tabla de multiplicar: "))
tabla_multiplicar(numero)
'''


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
'''
#Definicion de funciones:
def suma_a_b(num1, num2):
    return num1 + num2

def resta_a_b(num1, num2):
    return num1 - num2

def multiplicacion_a_b(num1, num2):
    return num1 * num2

def division_a_b(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "ERROR: No se puede dividir por 0!"
    
# Podria haber definido todo dentro de la funcion de operaciones_basicas pero opte por hacerlo asi para practura la excepcion cuando ingresan un "0" como parametro b

def operaciones_basicas(num1, num2):
    suma = suma_a_b(num1, num2)
    resta = resta_a_b(num1, num2)
    multiplicacion = multiplicacion_a_b(num1, num2)
    division = division_a_b(num1, num2)
    return (suma, resta, multiplicacion, division)
    # print(f'suma: {suma} \nresta: {resta} \nmultiplicacion: {multiplicacion} \ndivision: {division}')

# Programa principal:
a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))

suma, resta, multiplicacion, division = operaciones_basicas(a, b)

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
'''


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
'''
# Definicion de funciones:
def calcular_imc(peso, altura):
    return peso / (altura**2)


# Programa principal:
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en mts: "))

i_m_c = calcular_imc(peso, altura)

print(f'Su Indice de Masa Corporal es: {i_m_c}')
'''

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
'''
# Definicion de funciones:
def celsius_a_fahrenheit(celsius):
    return (celsius * (9/5) + 32)
# Podria poner tamnien asi: celcius * 1.8 + 32 ya que la prioridad va a ser resolver la multiplicacion y luego la suma, pero opte por poner la fraccion ya que asi aparece en los libros.

# Programa principal:
temp_c = float(input("Ingrese una temperatura en °c: "))

temp_f = celsius_a_fahrenheit(temp_c)

print(f'La temperatura ingresada equivale a {temp_f} grados Farenheit.')
'''


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.
'''
# Definicion de funciones:
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal:

# Los numeros los recibimos como flotantes ya que podria querer hacer la ecuacion con numeros no enteros:
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

promedio = calcular_promedio(num1, num2, num3)

print(f'El promedio de los tres numeros ingresados es: {promedio}')
'''