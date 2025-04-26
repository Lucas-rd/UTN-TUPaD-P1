# NOTA: Para probar el codigo, descomentar el ejercicio que se desa probar quitando las comillas ''' '''

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
'''
mi_lista = []

# Aqui decido recorrer una variable contador y evaluar cada valor del 1 al 100 para ver si es multiplo de 4. Si lo es, lo agrego con el metodo append en mi lista
for i in range (1, 101):
    if i % 4 == 0:
        mi_lista.append(i)

print(mi_lista)
'''

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
'''
mi_lista = [1, 2, 3, 4, 5]

# Muestro el penultimo valor con el indexing negativo "-2"
print(mi_lista[-2])
'''

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []
'''
mi_lista = []

# Hago una solucion un poco mas elegante para no tener que estar escribiendo 3 veces el metodo append
for i in range(1, 4):
    mi_lista.append(f'Palabra{i}')

print(mi_lista)
'''

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
'''
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"
print(animales)
'''

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
'''
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# Este codigo tiene dos funciones de listas anidadas una dentro de la otra. Por supuesto se resuelven "de adentro hacia afuera". Lo primero que hace es encontrar cual es el valor maximo de la lista y luego lo remueve con el .remove. Esto nos da como resultado la misma lista pero sin el valor maximo que en este caso es 22.

'''

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
'''
mi_lista = []

# Aprovecho la funcion del step del for para ir haciendo esos saltos de 5 en 5
for i in range(10, 31, 5):
    mi_lista.append(i)

# Con el slicing muestro los dos primeros elementos
print(mi_lista[0:2])
'''

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
'''
autos = ["sedan", "polo", "suran", "gol"]

# Como el ejercicio me da libertad del valor a ramplazar elegi poner dos valores booleanos
autos[1] = True
autos[2] = False

print(autos)
'''


# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
'''
dobles = []
# Lo hago con un for para evitar escribir 3 veces el metodo append
for i in range(5, 16, 5):
    dobles.append( i * 2 )

print(dobles)
'''


# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
    # a) Agregar "jugo" a la lista del tercer cliente usando append.
    # b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
    # c) Eliminar "pan" de la lista del primer cliente.
    # d) Imprimir la lista resultante por pantalla
'''
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)
'''


# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
    # ● Posición lista_anidada[0]: 15
    # ● Posición lista_anidada[1]: True
    # ● Posición lista_anidada[2][0]: 25.5
    # ● Posición lista_anidada[2][1]: 57.9
    # ● Posición lista_anidada[2][2]: 30.6
    # ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.
'''
lista_anidada = []

lista_anidada.append(15)
lista_anidada.append(True)
# Primero agrego una lista anidada vacia para luego poder ir agregando los siguientes valores que pide el enunciado
lista_anidada.append([])
lista_anidada[2].append(25.5)
lista_anidada[2].append(57.9)
lista_anidada[2].append(30.6)
lista_anidada.append(False)


print(lista_anidada)
'''