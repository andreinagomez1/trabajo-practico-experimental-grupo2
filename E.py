def ingresar_caracteres():
    pila = []
    while True:
        caracter = input("Ingrese un caracter: ")
        if caracter == '*':
            break
        elif caracter:  # Solo agregamos el carácter a la pila si no está vacío
            pila.append(caracter)
    return pila

def mostrar_elementos(pila):
    while pila:
        caracter = pila.pop()
        print(f"Caracter: {caracter}, Código ASCII: {ord(caracter)}")

def main():
    pila = ingresar_caracteres()
    mostrar_elementos(pila)

if __name__ == "__main__":
    main()

