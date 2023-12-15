def crear_matriz(n, m):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            while True:
                valor = input(f"Ingrese el valor para la posición {i+1},{j+1}: ")
                if valor.isdigit():
                    fila.append(int(valor))
                    break
                else:
                    print("Por favor, ingrese solo números.")
        matriz.append(fila)
    return matriz

def verificar_suma(matriz):
    suma_columna = sum(fila[0] for fila in matriz)
    for j in range(len(matriz[0])):
        if sum(fila[j] for fila in matriz) != suma_columna:
            return False
    return True

while True:
    n = input("Ingrese el valor de n: ")
    if n.isdigit() and int(n) != 0:
        n = int(n)
        break
    else:
        print("Por favor, ingrese un número distinto de cero.")

while True:
    m = input("Ingrese el valor de m: ")
    if m.isdigit() and int(m) != 0:
        m = int(m)
        break
    else:
        print("Por favor, ingrese un número distinto de cero.")

matriz = crear_matriz(n, m)

print("La matriz ingresada es:")
for fila in matriz:
    print(fila)

print()

if verificar_suma(matriz):
    print("La suma de cada columna es el mismo valor.")
else:
    print("La suma de cada columna no es el mismo valor.")
