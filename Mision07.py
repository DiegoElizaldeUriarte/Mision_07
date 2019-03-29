# Autor: Diego Raul Elizalde Uriarte
# Mision 07  Ciclos while

def dividir(dividendo, divisor):
    contador = 0
    less = dividendo
    while dividendo >= divisor:
        contador += 1
        dividendo -= divisor
    print(less, "/", divisor, "=", contador, ", sobra ", dividendo )


def encontrarMayor():
    a = int(input("Teclea un número [-1 para salir]: "))
    contador = 0
    while a != -1:
        if contador > a:
            a = int(input("Teclea un número [-1 para salir]: "))
        else:
            contador = a
            a = int(input("Teclea un número [-1 para salir]: "))
    print("El mayor es:", contador)


def main():
    a = int(input("""Misión 07. Ciclos while
Autor: Diego Raul Elizalde Uriarte
Matrícula: A01748756
1. Calcular divisiones
2. Encontrar el mayor
3. Salir
Teclea tu opción:"""))
    if a == 1:
        print("Calculando divisiones")
        dividendo = int(input("Dividendo: "))
        divisor = int(input("Divisor: "))
        dividir(dividendo, divisor)
    elif a == 2:
        print("Teclea una serie de números para encontrar el mayor.")
        encontrarMayor()
    else:
        pass






main()
