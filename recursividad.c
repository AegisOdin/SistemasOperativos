#include <stdio.h>

// Función para realizar la división usando sumas y restas
int division(int dividendo, int divisor) {
    if (divisor == 0) {
        printf("Error: División por cero.\n");
        return 0;
    }

    int cociente = 0;
    int esNegativo = 0;

    // Manejo de números negativos
    if (dividendo < 0) {
        dividendo = -dividendo;
        esNegativo = !esNegativo;
    }
    if (divisor < 0) {
        divisor = -divisor;
        esNegativo = !esNegativo;
    }

    while (dividendo >= divisor) {
        dividendo -= divisor;
        cociente++;
    }

    return esNegativo ? -cociente : cociente;
}

// Función para calcular la potencia usando sumas y restas
int exponente(int base, int exponente) {
    if (exponente < 0) {
        printf("Error: Exponente negativo no soportado.\n");
        return 0;
    }

    if (exponente == 0) {
        return 1;
    }

    int resultado = 1;
    for (int i = 0; i < exponente; i++) {
        int temp = 0;
        for (int j = 0; j < resultado; j++) {
            temp += base;
        }
        resultado = temp;
    }

    return resultado;
}

int main() {
    int dividendo, divisor, base, potencia;

    // Prueba de división
    printf("Introduce el dividendo: ");
    scanf("%d", &dividendo);
    printf("Introduce el divisor: ");
    scanf("%d", &divisor);

    int resultadoDivision = division(dividendo, divisor);
    printf("Resultado de la división: %d\n", resultadoDivision);

    // Prueba de exponente
    printf("Introduce la base: ");
    scanf("%d", &base);
    printf("Introduce el exponente: ");
    scanf("%d", &potencia);

    int resultadoExponente = exponente(base, potencia);
    printf("Resultado del exponente: %d\n", resultadoExponente);

    return 0;
}