def primera_cabida(particiones, procesos):

    asignaciones = [-1] * len(procesos)  
    
    # Recorrer todos los procesos
    for i in range(len(procesos)):
        for j in range(len(particiones)):
            
            if procesos[i] <= particiones[j]:
                
                asignaciones[i] = j
                
                particiones[j] -= procesos[i]
                break  
    
    return asignaciones

def mostrar_asignaciones(asignaciones, procesos, particiones):
    print("\nAsignación de procesos a particiones:")
    for i in range(len(asignaciones)):
        if asignaciones[i] != -1:
            print(f"Proceso {i+1} de tamaño {procesos[i]} KB asignado a partición {asignaciones[i]+1} de tamaño restante {particiones[asignaciones[i]]} KB")
        else:
            print(f"Proceso {i+1} de tamaño {procesos[i]} KB no ha sido asignado.")
    
    print("\nEstado final de las particiones:")
    for i in range(len(particiones)):
        print(f"Partición {i+1}: {particiones[i]} KB restante")

particiones = [500, 300, 700, 400, 600]  
procesos = [212, 417, 112, 426] 

asignaciones = primera_cabida(particiones, procesos)

mostrar_asignaciones(asignaciones, procesos, particiones)