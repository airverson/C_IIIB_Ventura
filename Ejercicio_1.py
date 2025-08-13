"""
Se realiza una calculadora con operaciones básicas : suma, resta y multiplicación
haciendo uso del ciclo while para repetir la acción al igual haciendo uso de funciones.

Realizado por Airverson Ventura 31/05/2025

"""

 
def DATOS(): #Definimos la función DATOS
 
    num1 = float(input("Ingresar el primer numero: ")) #Ingresamos el primer número
    num2 = float(input("Ingrese el segundo numero: ")) #Ingresamos el segundo número
    return num1, num2 #Retornamos el primer 1 y el segundo 2
 
def SUMA(): #Definimos suma
    print("SUMA") #Desplegar en pantalla suma
 
    num1, num2 = DATOS() #Llamamos a la función DATOS
    resultado = num1 + num2 #El resultado es igual al primer número más el segundo número
 
    print(f"\nRESULTADO: {num1} + {num2} = {resultado}") #Desplegar en pantalla el resultado es igual a num1 + num2
    input("Presione Enter para continuar...") #Desplegamos presionar enter para seguir en el programa

def RESTA(): #Definimos resta
    print("RESTA") #Desplegar en pantalla resta
 
    num1, num2 = DATOS() #Llamamos a la función DATOS
    resultado = num1 - num2 #El resultado es igual al primer número menos el segundo número
 
    print(f"\nRESULTADO: {num1} - {num2} = {resultado}")  #Desplegar en pantalla el resultado es igual a num1 - num2
    input("Presione Enter para continuar...") #Desplegamos presionar enter para seguir en el programa
 
def MULTIPLICACIÓN(): #Definimos multiplicación
    print("MULTIPLICACIÓN") #Desplegar en pantalla multiplicación
 
    num1, num2 = DATOS() #Llamamos a la función DATOS
    resultado = num1 * num2 #El resultado es igual al primer número por el segundo número
 
    print(f"\nRESULTADO: {num1} * {num2} = {resultado}") #Desplegar en pantalla el resultado es igual a num1 * num2
    input("Presione Enter para continuar...") #Desplegamos presionar enter para seguir en el programa


while True: #Ciclo while para repetir acciones
    print("Seleccione una opcion") #Seleccione una opción
    print("1. SUMA") #Opción 1 suma
    print("2. RESTA") #Opción 2 resta
    print("3. MULTIPLICACIÓN") #Opción 3 multiplicación
    print("4. Salir") #Opción 5 para salir del programa
    opcion = input("Ingrese el numero de la opcion deseada: ") #Ingresa opción deseada
 
    if opcion == '1': #opcion 1 para sumar
        SUMA() #Se llama a SUMA para sumar

    elif opcion == '2': #opcion 2 para restar
        RESTA() #Se llama RESTA para restar

    elif opcion == '3': #opcion 3 para multiplicar
        MULTIPLICACIÓN() #Se llama a MULTIPLICACIÓN para multiplicar

    elif opcion == '4': #opcion 5 para salir del programa
        print("\nSaliendo del sistema... ¡Hasta luego!") #Deplegamos para salir del programa
        break #Descanso
    else: #Si no
        print("opcion no valida.") #La opción no es válida