import random

#Escribe un programa que simule una tabla de páginas para procesos  con acceso aleatorio a memoria virtual.

class SistemaMemoria:
    def __init__(self, tam_memoria_virtual, tam_memoria_fisica, tam_pagina):
        self.tam_pagina = tam_pagina
        self.tam_memoria_virtual = tam_memoria_virtual
        self.tam_memoria_fisica = tam_memoria_fisica
        self.memoria_virtual = [None] * (tam_memoria_virtual // tam_pagina)  
        self.memoria_fisica = [None] * (tam_memoria_fisica // tam_pagina)  
        self.tabla_paginas = {} 

    def cargar_pagina(self, pagina_virtual):
        """Cargar la página virtual en un marco físico disponible."""
        for marco in range(len(self.memoria_fisica)):
            if self.memoria_fisica[marco] is None:
                self.memoria_fisica[marco] = pagina_virtual
                self.tabla_paginas[pagina_virtual] = marco
                print(f"Cargando página virtual {pagina_virtual} en marco físico {marco}.")
                return
        print("No hay espacio físico disponible para cargar la página.")

    def acceso_memoria_virtual(self, direccion_virtual):
        """Simula el acceso a la memoria virtual mediante una tabla de páginas."""
        pagina_virtual = direccion_virtual // self.tam_pagina  
        desplazamiento = direccion_virtual % self.tam_pagina  

        if pagina_virtual in self.tabla_paginas:
            marco_fisico = self.tabla_paginas[pagina_virtual]
            direccion_fisica = marco_fisico * self.tam_pagina + desplazamiento
            print(f"Accediendo a dirección virtual {direccion_virtual} (Página {pagina_virtual}), "
                  f"correspondiente a la dirección física {direccion_fisica}.")
        else:
            print(f"Página virtual {pagina_virtual} no cargada. Cargando ahora...")
            self.cargar_pagina(pagina_virtual)
            self.acceso_memoria_virtual(direccion_virtual)


tam_memoria_virtual = 1024  
tam_memoria_fisica = 512   
tam_pagina = 128          


sistema_memoria = SistemaMemoria(tam_memoria_virtual, tam_memoria_fisica, tam_pagina)

for _ in range(10):
    direccion_virtual = random.randint(0, tam_memoria_virtual - 1)  
    sistema_memoria.acceso_memoria_virtual(direccion_virtual)
