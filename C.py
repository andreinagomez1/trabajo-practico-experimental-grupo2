def reemplazar_por_asterisco(lista, n):
    for i in range(len(lista)):
        if lista[i] == n:
            lista[i] = '*'
    return lista
def es_lista_de_enteros(lista):
    return all(isinstance(i, int) for i in lista)
while True:
    lista = input("Ingrese una lista de números enteros, separados por comas: ")
    lista = lista.split(',')
    lista = [i.strip() for i in lista]
    if all(i.isdigit() for i in lista):
        lista = [int(i) for i in lista]
        break
    else:
        print("Por favor, ingrese solo números enteros.")
while True:
    n = input("Ingrese un número entero: ")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Por favor, ingrese un número entero.")

lista = reemplazar_por_asterisco(lista, n)
print("La lista modificada es:")
print(lista)
