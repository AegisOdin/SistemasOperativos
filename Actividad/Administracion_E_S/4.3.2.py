import random
import time

#Escribe un programa que simule las operaciones de un manejador de dispositivos utilizando una tabla de estructuras.


class Dispositivo:
    """Clase que representa un dispositivo con sus propiedades y funciones."""
    
    def __init__(self, id, tipo, estado="inactivo"):
        self.id = id
        self.tipo = tipo 
        self.estado = estado 
    
    def leer(self):
        """Simula una operación de lectura del dispositivo."""
        if self.estado == "activo":
            print(f"[{self.tipo}] Dispositivo {self.id} está leyendo datos.")
        else:
            print(f"[{self.tipo}] Dispositivo {self.id} está inactivo, no puede leer datos.")
    
    def escribir(self, dato):
        """Simula una operación de escritura en el dispositivo."""
        if self.estado == "activo":
            print(f"[{self.tipo}] Dispositivo {self.id} está escribiendo datos: {dato}")
        else:
            print(f"[{self.tipo}] Dispositivo {self.id} está inactivo, no puede escribir datos.")
    
    def activar(self):
        """Activa el dispositivo."""
        self.estado = "activo"
        print(f"[{self.tipo}] Dispositivo {self.id} ha sido activado.")
    
    def desactivar(self):
        """Desactiva el dispositivo."""
        self.estado = "inactivo"
        print(f"[{self.tipo}] Dispositivo {self.id} ha sido desactivado.")

class ManejadorDeDispositivos:
    """Clase que simula un manejador de dispositivos."""
    
    def __init__(self):
        self.tabla_de_dispositivos = []
    
    def agregar_dispositivo(self, dispositivo):
        """Agrega un dispositivo a la tabla de dispositivos."""
        self.tabla_de_dispositivos.append(dispositivo)
        print(f"Dispositivo {dispositivo.id} de tipo {dispositivo.tipo} agregado a la tabla.")
    
    def operar_dispositivo(self, id_dispositivo, operacion, dato=None):
        """Realiza una operación sobre el dispositivo con el ID dado."""
        dispositivo = self.buscar_dispositivo(id_dispositivo)
        if dispositivo:
            if operacion == "leer":
                dispositivo.leer()
            elif operacion == "escribir" and dato:
                dispositivo.escribir(dato)
            else:
                print("Operación no válida.")
        else:
            print(f"Dispositivo con ID {id_dispositivo} no encontrado.")
    
    def buscar_dispositivo(self, id_dispositivo):
        """Busca un dispositivo en la tabla por su ID."""
        for dispositivo in self.tabla_de_dispositivos:
            if dispositivo.id == id_dispositivo:
                return dispositivo
        return None
    
    def activar_dispositivo(self, id_dispositivo):
        """Activa el dispositivo con el ID dado."""
        dispositivo = self.buscar_dispositivo(id_dispositivo)
        if dispositivo:
            dispositivo.activar()
        else:
            print(f"Dispositivo con ID {id_dispositivo} no encontrado.")
    
    def desactivar_dispositivo(self, id_dispositivo):
        """Desactiva el dispositivo con el ID dado."""
        dispositivo = self.buscar_dispositivo(id_dispositivo)
        if dispositivo:
            dispositivo.desactivar()
        else:
            print(f"Dispositivo con ID {id_dispositivo} no encontrado.")

def simular_manejo_de_dispositivos():
    manejador = ManejadorDeDispositivos()

    dispositivo1 = Dispositivo(id=1, tipo="disco")
    dispositivo2 = Dispositivo(id=2, tipo="impresora")
    dispositivo3 = Dispositivo(id=3, tipo="teclado")
    
    manejador.agregar_dispositivo(dispositivo1)
    manejador.agregar_dispositivo(dispositivo2)
    manejador.agregar_dispositivo(dispositivo3)

    manejador.activar_dispositivo(1)  # Activar disco
    manejador.activar_dispositivo(2)  # Activar impresora

    manejador.operar_dispositivo(1, "leer")
    manejador.operar_dispositivo(2, "escribir", "Mensaje de impresión")
    manejador.operar_dispositivo(3, "leer") 

    manejador.desactivar_dispositivo(1) 

    
    manejador.operar_dispositivo(1, "leer") 
    manejador.operar_dispositivo(1, "escribir", "Nuevo dato")

if __name__ == "__main__":
    simular_manejo_de_dispositivos()
