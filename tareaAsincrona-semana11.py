#Asincrona Semana 11
'''Se solicita crear un programa que permita recibir como datos N números naturales, determine cuántos de ellos son positivos,
negativos o nulos.

Si el usuario escribe un dato incorrecto, el programa no se ejecutará, en cambio preguntará de nuevo por la información hasta que
el dato ingresado sea correcto.
'''
# Inicio del codigo
print("--------------------------------------------------")
print("== Bienvenido Ing. a nuestro programa ==")
print("--------------------------------------------------\n")

print("Inicio del programa.\n")
print('''Ingrese los datos que se le pidan para determinar si esos números son: 
      Positivos, Negativos o Nulos \n''')


#Establecer datos y pedir los restantes
#Estructurar un def para evitar que el programa se rompa si el usuario se equivoca
def validar_letras(Evaluar):

    while True:
        try:
            valor = int(input(Evaluar))
            return valor
        except ValueError:
            print("Por favor, ingrese un número entero que sea válido.")


cantidad_numeros = validar_letras("Ingrese la cantidad de números que desea procesar en el programa: ")
#variables para que cuenten la cantidad de números puestos de su tipo
positivos = 0
negativos = 0
nulos = 0
#for para realizar el contador
for i in range(cantidad_numeros):
    numero = validar_letras(f"Ingrese el número {i+1}: ")
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        nulos += 1

print(f"Resultados: {positivos} números positivos, {negativos} números negativos, {nulos} números nulos.")

#indicar el fin del programa
print("\nFin del programa\n")