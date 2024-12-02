import random
import time

# Realiza una simulación en cualquier lenguaje de programación que  emule el swapping de procesos en memoria virtual.


class Proceso:
    def __init__(self, id_proceso):
        self.id_proceso = id_proceso
        self.en_swap = False  
        self.ultimo_acceso = time.time()  

    def __str__(self):
        return f"Proceso {self.id_proceso}"

class SistemaMemoriaVirtual:
    def __init__(self, tamano_ram, tamano_swap):
        self.ram = []
        self.swap = []
        self.tamano_ram = tamano_ram
        self.tamano_swap = tamano_swap
    
    def cargar_proceso(self, proceso):
        """Cargar un proceso en la memoria RAM o realizar un swap si la RAM está llena."""
        if len(self.ram) < self.tamano_ram:
            self.ram.append(proceso)
            print(f"{proceso} cargado en RAM.")
        else:
            self.swap_proceso(proceso)
    
    def swap_proceso(self, nuevo_proceso):
        """Realiza el swap de un proceso, moviendo uno de la RAM al swap."""
        proceso_a_swap = min(self.ram, key=lambda p: p.ultimo_acceso)
        self.ram.remove(proceso_a_swap)
        self.swap.append(proceso_a_swap)
        proceso_a_swap.en_swap = True
        print(f"{proceso_a_swap} movido al espacio swap.")
        
        self.ram.append(nuevo_proceso)
        print(f"{nuevo_proceso} cargado en RAM.")

    def acceder_proceso(self, id_proceso):
        """Simula el acceso a un proceso, actualizando su tiempo de acceso."""
        proceso_en_ram = next((p for p in self.ram if p.id_proceso == id_proceso), None)
        if proceso_en_ram:
            proceso_en_ram.ultimo_acceso = time.time()
            print(f"Accediendo a {proceso_en_ram} en RAM.")
        else:
            proceso_en_swap = next((p for p in self.swap if p.id_proceso == id_proceso), None)
            if proceso_en_swap:
                print(f"Accediendo a {proceso_en_swap} en swap. Moviéndolo de vuelta a RAM.")
                self.swap.remove(proceso_en_swap)
                self.ram.append(proceso_en_swap)
                proceso_en_swap.en_swap = False
                proceso_en_swap.ultimo_acceso = time.time()
            else:
                print(f"Proceso {id_proceso} no encontrado.")
        
    def mostrar_estado(self):
        """Mostrar el estado actual de la RAM y el swap."""
        print("\nEstado del sistema:")
        print("RAM:")
        for p in self.ram:
            print(f"- {p}")
        print("Swap:")
        for p in self.swap:
            print(f"- {p}")
        print("\n")

def simulacion():
    tamano_ram = 3  
    tamano_swap = 5  
    
    sistema = SistemaMemoriaVirtual(tamano_ram, tamano_swap)
    
    procesos = [Proceso(i) for i in range(1, 8)]
    
    for p in procesos:
        sistema.cargar_proceso(p)
        sistema.mostrar_estado()
        time.sleep(1) 

    sistema.acceder_proceso(3)
    time.sleep(2)
    sistema.acceder_proceso(5)
    time.sleep(1)
    sistema.acceder_proceso(1)
    time.sleep(1)
    
    sistema.mostrar_estado()
    
    nuevo_proceso = Proceso(8)
    sistema.cargar_proceso(nuevo_proceso)
    sistema.mostrar_estado()

if __name__ == "__main__":
    simulacion()
