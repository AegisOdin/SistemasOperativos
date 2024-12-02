# Administración de Memoria Virtual en Linux

La administración de memoria virtual en sistemas operativos modernos, como **Linux**, es crucial para garantizar el rendimiento eficiente de los procesos, la multitarea y la protección de memoria entre diferentes aplicaciones. Linux maneja tanto la memoria física como la memoria virtual para proporcionar un entorno robusto de ejecución.

## 1. Concepto de Memoria Virtual en Linux

La **memoria virtual** permite que los procesos accedan a direcciones de memoria que no corresponden necesariamente a ubicaciones físicas en la RAM. Utiliza una **tabla de páginas** y un **mecanismo de intercambio** (swap) para lograr esta abstracción. La memoria virtual permite a los procesos tener su propio espacio de direcciones, protegiéndolos unos de otros y mejorando la eficiencia de uso de la memoria.

## 2. Espacio de Direcciones Virtuales

Cada proceso en Linux tiene su propio espacio de direcciones virtuales. Este espacio es gestionado por el sistema operativo para asegurar que no haya solapamientos de direcciones entre procesos. La estructura general de la dirección virtual se divide en varias secciones:

- **Código** (Texto): Almacena el código ejecutable del proceso.
- **Datos**: Contiene la información dinámica, como variables globales.
- **Pila** (Stack): Se utiliza para el almacenamiento de variables locales y el seguimiento de las funciones (funciones de llamada).
- **Heap**: Área utilizada para la asignación dinámica de memoria (por ejemplo, `malloc`).
- **Mapa de Memoria Compartida**: Si el proceso comparte memoria con otros, esta área se utiliza.

## 3. Tabla de Páginas y Traducción de Direcciones

La memoria virtual se gestiona en **páginas**, que son unidades de tamaño fijo (generalmente 4 KB en arquitecturas de 32 bits). Cada dirección virtual es dividida en dos partes:

1. **Número de Página Virtual (VPN)**: La parte de la dirección virtual que se usa para buscar en la tabla de páginas.
2. **Desplazamiento (Offset)**: La parte de la dirección que se refiere a una posición dentro de la página.

El sistema operativo utiliza una **tabla de páginas** para realizar la traducción entre las direcciones virtuales y las físicas. Esta tabla se encuentra en la memoria virtual y es gestionada por el **MMU** (Unidad de Gestión de Memoria) en el hardware, que busca la entrada correspondiente para realizar la conversión.

Si un proceso intenta acceder a una página que no está mapeada en la memoria física (por ejemplo, si se ha paginado en el disco), se genera un **fallo de página** (page fault), y el sistema operativo gestiona la carga de la página desde el disco a la memoria.

## 4. Paginación y Mecanismo de Fallo de Página

### Paginación
Cuando un proceso accede a una dirección virtual, el sistema operativo consulta la tabla de páginas para ver si la página correspondiente está en la memoria física. Si la página no está presente, el sistema operativo genera un fallo de página y carga la página desde el espacio de intercambio (swap) o desde el almacenamiento secundario.

### Fallo de Página
Cuando un proceso accede a una página que no está cargada en la memoria, el sistema operativo gestiona un fallo de página. Esto implica:
1. **Interrupción del proceso**.
2. **Carga de la página** desde el espacio de intercambio o disco a la memoria física.
3. **Reanudación del proceso** con la página cargada.

## 5. Intercambio (Swap) y Memoria Virtual

Linux utiliza el **swap** como una forma de extender la memoria física. Cuando la memoria RAM está llena, las páginas menos utilizadas se pueden mover a una **zona de intercambio** en el disco duro (el espacio swap). Este mecanismo permite que los procesos sigan ejecutándose incluso cuando la memoria física es insuficiente.

### Proceso de intercambio
- Cuando se agota la memoria RAM, el sistema selecciona páginas que no se han usado recientemente y las mueve al espacio swap.
- Si un proceso necesita esas páginas, se realizan más fallos de página, y las páginas se trasladan de vuelta a la memoria RAM, posiblemente desechando otras menos utilizadas.

## 6. Protección y Aislamiento de Memoria

Linux utiliza la memoria virtual para aislar a los procesos entre sí, asegurando que un proceso no pueda acceder a la memoria de otro sin permiso. Esto se logra mediante el uso de tablas de páginas, donde las entradas de la tabla pueden marcarse como de solo lectura, de solo escritura, o de ejecución (mediante los bits de protección).

### Protección de memoria:
- **No escritura**: Un proceso no puede escribir en una página de solo lectura.
- **No ejecución**: Algunas páginas (como las pilas) pueden marcarse como no ejecutables para prevenir ataques de desbordamiento de pila.
- **Aislamiento de procesos**: Cada proceso tiene un espacio de direcciones virtuales independiente. Un proceso no puede acceder a la memoria de otro sin pasar por mecanismos de comunicación interprocesos (IPC).

## 7. Implementación de la Memoria Virtual en Linux

En Linux, la memoria virtual se implementa mediante la siguiente infraestructura:

- **MMU (Unidad de Gestión de Memoria)**: El hardware que realiza la traducción de direcciones virtuales a físicas, utilizando las tablas de páginas.
- **Tabla de Páginas**: Se utiliza para gestionar las direcciones virtuales y su correspondencia con la memoria física.
- **Swap**: Un espacio de almacenamiento en disco utilizado para extender la memoria virtual, cargando y descargando páginas de la memoria RAM según sea necesario.

## 8. Mecanismos de Optimización y Configuración en Linux

Linux permite configurar varios parámetros relacionados con la gestión de la memoria virtual para optimizar el rendimiento, tales como:

- **Swappiness**: Controla la agresividad con la que el sistema operativo mueve las páginas a swap. Un valor bajo significa que se usará menos swap.
- **Overcommit Handling**: Linux puede configurar políticas para cómo manejar la solicitud de memoria cuando la memoria física es insuficiente.
- **Huge Pages**: Para aplicaciones que requieren grandes cantidades de memoria, Linux ofrece soporte para páginas de mayor tamaño, lo que reduce la sobrecarga de la gestión de memoria.

## Codigo

```python
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
