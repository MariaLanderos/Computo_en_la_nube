from ExamenU1 import (num_primo,
                      next_prime,
                      median_of_three,
                      generate_random_password,
                      calcular_hipotenusa
                      
)


if __name__ == "__main__":


#Ejercicio 1
    user_input = int(input("Ingresa un número entero: "))
    if num_primo(user_input):
        print(f"{user_input} es un número primo.")
    else:
        print(f"{user_input} no es un número primo.")

#Ejercicio2

    user_input2 = int(input("Ingresa un número entero: "))
    prime = next_prime(user_input2)
    print(f"El primer número primo mayor que {user_input2} es {prime}.")

#Ejercicio 3 
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))
    median = median_of_three(num1, num2, num3)
    print(f"La mediana de los números ingresados es {median}.")

#Ejercicio 4

    random_password = generate_random_password()
    print(f"Contraseña generada aleatoriamente: {random_password}")

#Ejercicio 5 
    lado1 = float(input("Ingresa la longitud del primer lado: "))
    lado2 = float(input("Ingresa la longitud del segundo lado: "))
    hipotenusa = calcular_hipotenusa(lado1, lado2)
    print(f"La longitud de la hipotenusa es {hipotenusa}.")