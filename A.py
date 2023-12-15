def crear_matriz(n):
    return [[i + j * n for i in range(n)] for j in range(n)]

while True:
    n = input("Ingrese el valor de n: ")
    if n.isdigit() and int(n) != 0:
        n = int(n)
        matriz = crear_matriz(n)
        for fila in matriz:
            print(fila)
        break
    else:
        print("Por favor, ingrese solo números o numeros diferentes de 0.")
