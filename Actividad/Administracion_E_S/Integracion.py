import random
import time
from queue import Queue

class Dispositivo:
    """Clase base para los dispositivos."""
    
    def __init__(self, id, tipo):
        self.id = id 
        self.tipo = tipo  # Tipo de dispositivo (disco, impresora, teclado)
    
    def operar(self):
        """Método abstracto para realizar una operación. Debe ser implementado por cada dispositivo."""
        raise NotImplementedError("El método operar debe ser implementado en cada dispositivo.")
    
    def __str__(self):
        return f"[{self.tipo}] Dispositivo {self.id}"

class Teclado(Dispositivo):
    def __init__(self, id):
        super().__init__(id, "Teclado")
    
    def operar(self, cola):
        """Simula la captura de texto y lo coloca en la cola de operaciones."""
        texto = f"Texto generado por el Teclado {self.id}: {random.choice(['Hola', 'Adiós', 'Python', 'Dispositivos', 'Simulación'])}"
        print(f"{self} captura texto: {texto}")
        cola.put(texto)  

class DiscoDuro(Dispositivo):
    def __init__(self, id):
        super().__init__(id, "Disco Duro")
    
    def operar(self, cola):
        """Simula la lectura de la cola y el almacenamiento de los datos en el disco."""
        if not cola.empty():
            texto = cola.get()  
            print(f"{self} almacena en disco: {texto}")
            return texto  
        return None

class Impresora(Dispositivo):
    def __init__(self, id):
        super().__init__(id, "Impresora")
    
    def operar(self, contenido):
        """Simula la impresión del contenido del disco."""
        if contenido:
            print(f"{self} imprime: {contenido}")
        else:
            print(f"{self} no tiene contenido para imprimir.")

class ManejadorDeDispositivos:
    def __init__(self):
        self.devices = [] 
        self.cola = Queue() 
    
    def agregar_dispositivo(self, dispositivo):
        """Agrega un dispositivo al sistema."""
        self.devices.append(dispositivo)
        print(f"Dispositivo {dispositivo} agregado al sistema.")
    
    def ejecutar_operaciones(self):
        """Ejecuta las operaciones de los dispositivos: Teclado -> Disco -> Impresora."""
        contenido = None
        
        for dispositivo in self.devices:
            if isinstance(dispositivo, Teclado):
                dispositivo.operar(self.cola)
            elif isinstance(dispositivo, DiscoDuro):
                contenido = dispositivo.operar(self.cola)
            elif isinstance(dispositivo, Impresora):
                dispositivo.operar(contenido)

def simular_sistema():
    manejador = ManejadorDeDispositivos()
    
    teclado = Teclado(id=1)
    disco = DiscoDuro(id=1)
    impresora = Impresora(id=1)
    
    manejador.agregar_dispositivo(teclado)
    manejador.agregar_dispositivo(disco)
    manejador.agregar_dispositivo(impresora)
    
    print("\nSimulación de operaciones de dispositivos:")
    manejador.ejecutar_operaciones()

if __name__ == "__main__":
    simular_sistema()
