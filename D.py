from collections import deque

class Cola:
    def __init__(self):
        self.cola = deque()
        self.suma = 0
        self.contador = 0

    def agregar_numero(self, numero):
        self.cola.append(numero)
        self.suma += numero
        self.contador += 1

    def calcular_promedio(self):
        return self.suma / self.contador if self.contador != 0 else 0

    def mostrar_elementos(self):
        while self.cola:
            print(self.cola.popleft())

cola = Cola()

while True:
    numero = input("Ingrese un número entero (0 para terminar): ")
    if numero.isdigit() or (numero.startswith('-') and numero[1:].isdigit()):
        numero = int(numero)
        if numero == 0:
            break
        cola.agregar_numero(numero)
    else:
        print("Por favor, ingrese solo números enteros.")

print("Los elementos ingresados a la cola son:")
cola.mostrar_elementos()
print("El promedio de los números ingresados es:", cola.calcular_promedio())
