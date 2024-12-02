# Diseña un sistema que maneje múltiples dispositivos simulados (disco duro, impresora, teclado) y muestra cómo se realiza la comunicación entre ellos.

**Componentes del Sistema:**
1. Clase Dispositivo: Es la clase base para todos los dispositivos (disco duro, impresora y teclado). Define los métodos generales que cada dispositivo debe tener.

2. Clase DiscoDuro, Impresora, y Teclado: Son clases derivadas de Dispositivo que simulan el comportamiento de cada tipo de dispositivo específico.

3. Clase Controlador: Es la clase que administra las solicitudes de E/S y la comunicación entre el sistema operativo y los dispositivos.

4. Clase SistemaOperativo: Es la clase principal que orquesta todo el proceso. El sistema operativo se comunica con los dispositivos a través de su controlador y maneja las solicitudes de E/S.

**PSEUDOCODIGO:**

*Clase base para Dispositivos*
Clase Dispositivo:
    Atributos:
        nombre (Nombre del dispositivo)
        cola_solicitudes (Lista de solicitudes de E/S)
    
    Métodos:
        agregar_solicitud(solicitud):
            Agregar una solicitud a la cola de solicitudes

        procesar_solicitudes():
            Mientras haya solicitudes en la cola_solicitudes:
                Solicitud = quitar_solicitud()
                procesar_solicitud(Solicitud)

*Clase para simular un Disco Duro*
Clase DiscoDuro hereda de Dispositivo:
    Métodos:
        procesar_solicitud(solicitud):
            Imprimir "Procesando solicitud de disco: " + solicitud
            # Simulamos lectura/escritura de datos del disco

*Clase para simular una Impresora*
Clase Impresora hereda de Dispositivo:
    Métodos:
        procesar_solicitud(solicitud):
            Imprimir "Imprimiendo: " + solicitud
            # Simulamos la acción de impresión

*Clase para simular un Teclado*
Clase Teclado hereda de Dispositivo:
    Métodos:
        procesar_solicitud(solicitud):
            Imprimir "Teclado: Recibiendo entrada de usuario: " + solicitud
            # Simulamos la entrada de datos del teclado

*Clase Controlador de Dispositivos*
Clase Controlador:
    Atributos:
        dispositivos (Lista de dispositivos)

    Métodos:
        registrar_dispositivo(dispositivo):
            Agregar dispositivo a la lista de dispositivos

        procesar_peticiones():
            Para cada dispositivo en dispositivos:
                dispositivo.procesar_solicitudes()

*Clase Sistema Operativo*
Clase SistemaOperativo:
    Atributos:
        controlador (Instancia de Controlador)
    
    Métodos:
        crear_solicitud(tipo_dispositivo, solicitud):
            Dependiendo del tipo_dispositivo, crear la solicitud y agregarla al dispositivo correspondiente
            controlador.registrar_dispositivo(tipo_dispositivo)

        iniciar_sistema():
            controlador.procesar_peticiones()

*Simulación del Sistema*
sistema = SistemaOperativo()
controlador = Controlador()

*Crear los dispositivos simulados*
disco = DiscoDuro(nombre="Disco Duro 1")
impresora = Impresora(nombre="Impresora 1")
teclado = Teclado(nombre="Teclado 1")

*Registrar los dispositivos en el controlador*
controlador.registrar_dispositivo(disco)
controlador.registrar_dispositivo(impresora)
controlador.registrar_dispositivo(teclado)

*Crear algunas solicitudes de E/S*
sistema.crear_solicitud(disco, "Leer archivo.txt")
sistema.crear_solicitud(impresora, "Imprimir documento1.pdf")
sistema.crear_solicitud(teclado, "Escribir mensaje de usuario")

*Iniciar el sistema operativo para procesar las solicitudes*
sistema.iniciar_sistema()

# Codigo

```python 
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

