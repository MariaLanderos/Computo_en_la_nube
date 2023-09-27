#Ejercicio 1 Número primo
'''
¿Es un número primo?
Un número primo es un entero mayor que 1 que solo es divisible por uno y por sí mismo.
Escribe una función que determine si su parámetro es primo o no, devolviendo True si lo es
 y False en caso contrario. Escribe un programa principal que lea un entero del usuario 
 y muestre un mensaje indicando si es primo o no. Asegúrate de que el programa principal 
 no se ejecute si el archivo que contiene tu solución se importa en otro programa.
'''
import random

def num_primo(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True


#Ejercicio 2  Próximo número primo (usando la función del Ejercicio 1)

def next_prime(n):
    n += 1
    while True:
        if num_primo(n):
            return n
        n += 1

#Ejercicio 3 Mediana de tres valores
def median_of_three(num1, num2, num3):
    nums = [num1, num2, num3]
    nums.sort()
    return nums[1]

#Ejercicio 4 Contraseña aleatoria
import string
def generate_random_password():
    length = random.randint(7, 10)  # Generamos un número aleatorio entre 7 y 10 (longitud de la contraseña).
    # Usamos una comprensión de listas para crear una cadena de caracteres aleatorios.
    # 'random.choice(string.printable[33:127])' elige un carácter aleatorio de los caracteres imprimibles ASCII
    # que van desde el índice 33 al 126.
    # Repetimos esto 'length' veces para construir la contraseña.
    password = ''.join(random.choice(string.printable[33:127]) for _ in range(length))
    return password

#Ejercicio 5 Calcular la hipotenusa
import math
def calcular_hipotenusa(side1, side2):
    hipotenusa = math.sqrt(side1**2 + side2**2)
    return hipotenusa