class Colas:
    def __init__(self):
        self.cola1 = []

    def encolar(self, item):
        self.cola1.append(item)

    def desencolar(self):
        try:
            return self.cola1.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

    def vacia(self):
        return len(self.cola1) == 0

class Servicios:
    def __init__(self):
        self.colas = {}

    def llegada_cliente(self, numero_servicio):
        if numero_servicio not in self.colas:
            self.colas[numero_servicio] = Colas()
        num_atencion = len(self.colas[numero_servicio].cola1) + 1
        self.colas[numero_servicio].encolar(num_atencion)
        print(f"El cliente {num_atencion} va en la cola {numero_servicio}")
        print(f"La cola {numero_servicio}: {self.colas[numero_servicio].cola1}")

    def atencion_cliente(self, numero_servicio):
        if numero_servicio in self.colas and not self.colas[numero_servicio].vacia():
            numero_atencion = self.colas[numero_servicio].desencolar()
            print(f"El cliente {numero_atencion} de la cola {numero_servicio} ya fue atendido")
            print(f"La cola {numero_servicio}: {self.colas[numero_servicio].cola1}")
        else:
            print(f"No hay clientes para atender en el servicio {numero_servicio}")
           

def main():
    servicio = Servicios()
    while True:
        comando = input("Ingrese un comando (C/A) seguido del número de servicio (Ejemplo: C22): ").strip().upper()
        if comando and comando[0] in ['C', 'A'] and len(comando) > 1:
            try:
                num_servicio = int(comando[1:])
                if comando[0] == 'C':
                    servicio.llegada_cliente(num_servicio)
                elif comando[0] == 'A':
                    servicio.atencion_cliente(num_servicio)
            except ValueError:
                print("El número de servicio debe ser un número válido.")
        elif comando == 'SALIR':
            break
        else:
            print("Comando no reconocido. Use 'C' para llegada de cliente o 'A' para atender cliente.")

if __name__ == "__main__":
    main()
