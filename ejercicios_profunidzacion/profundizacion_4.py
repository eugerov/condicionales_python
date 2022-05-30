# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
print('Ingrese palabra 1:')
palabra_1 = str(input())
print('Ingrese palabra 2:')
palabra_2 = str(input())
print('Ingrese palabra 3:')
palabra_3 = str(input())
print('Si queire Ordenar por orden alfabético, Ingrese opcion 1.')
print('Si quiere Ordenar por cantidad de letras Ingrese opcion 2:')     
opcion = int(input())

#if opcion == 1:
my_list=str()
my_list = palabra_1,palabra_2,palabra_3
sorted_list = sorted(my_list)
print(sorted_list)
#else:
texto_1 = len(palabra_1)                                      
texto_2 = len(palabra_2)
texto_3 = len(palabra_2)
list = texto_1,texto_2,texto_3
sorted_list1 = sorted(list)
print(sorted_list1)
