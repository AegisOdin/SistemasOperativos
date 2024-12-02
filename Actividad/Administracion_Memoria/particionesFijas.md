# Codigo

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX_PARTITIONS 100

typedef struct {
    int size;
    int is_allocated;
} Partition;

int main() {
    int total_memory_size, num_partitions;
    Partition partitions[MAX_PARTITIONS];

    // Solicitar el tamaño total de la memoria
    printf("Ingrese el tamaño total de la memoria (en KB): ");
    scanf("%d", &total_memory_size);

    // Solicitar el número de particiones
    printf("Ingrese el número de particiones: ");
    scanf("%d", &num_partitions);

    if (num_partitions > MAX_PARTITIONS) {
        printf("El número máximo de particiones es %d\n", MAX_PARTITIONS);
        return 1;
    }

    // Solicitar el tamaño de cada partición
    int total_partition_size = 0;
    for (int i = 0; i < num_partitions; i++) {
        printf("Ingrese el tamaño de la partición %d (en KB): ", i + 1);
        scanf("%d", &partitions[i].size);
        partitions[i].is_allocated = 0;
        total_partition_size += partitions[i].size;
    }

    // Verificar si el tamaño total de las particiones excede el tamaño total de la memoria
    if (total_partition_size > total_memory_size) {
        printf("Error: El tamaño total de las particiones excede el tamaño total de la memoria disponible.\n");
        return 1;
    }

    // Mostrar el estado de las particiones
    printf("\nEstado inicial de las particiones:\n");
    for (int i = 0; i < num_partitions; i++) {
        printf("Partición %d: Tamaño = %d KB, Estado = %s\n", i + 1, partitions[i].size, partitions[i].is_allocated ? "Asignada" : "Libre");
    }

    // Simular la asignación de memoria
    char option;
    do {
        int partition_number;
        printf("\nIngrese el número de la partición que desea asignar/liberar (1-%d): ", num_partitions);
        scanf("%d", &partition_number);

        if (partition_number < 1 || partition_number > num_partitions) {
            printf("Número de partición inválido.\n");
        } else {
            partition_number--; // Ajustar índice
            if (partitions[partition_number].is_allocated) {
                printf("Liberando la partición %d...\n", partition_number + 1);
                partitions[partition_number].is_allocated = 0;
            } else {
                printf("Asignando la partición %d...\n", partition_number + 1);
                partitions[partition_number].is_allocated = 1;
            }
        }

        // Mostrar el estado actualizado de las particiones
        printf("\nEstado actualizado de las particiones:\n");
        for (int i = 0; i < num_partitions; i++) {
            printf("Partición %d: Tamaño = %d KB, Estado = %s\n", i + 1, partitions[i].size, partitions[i].is_allocated ? "Asignada" : "Libre");
        }

        // Preguntar si el usuario desea continuar
        printf("\nDesea continuar? (s/n): ");
        scanf(" %c", &option);
    } while (option == 's' || option == 'S');

    return 0;
}
