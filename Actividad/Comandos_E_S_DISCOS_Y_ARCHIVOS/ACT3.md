# Copiar y Mover Archivos

## Objetivo
Practicar copiar y mover archivos y directorios.

## COMANDOS:

```bash
vboxuser@uwuntu:~/Desktop$       echo "Este es un archivo de prueba" > archivo1.txt
vboxuser@uwuntu:~/Desktop$   cp archivo1.txt /Prueba/
cp: cannot create regular file '/Prueba/': Not a directory
vboxuser@uwuntu:~/Desktop$ cp archivo1.txt /tmp/
vboxuser@uwuntu:~/Desktop$ mv /tmp/archivo1.txt /tmp/archivo2.txt
vboxuser@uwuntu:~/Desktop$   mv /tmp/archivo2.txt .
vboxuser@uwuntu:~/Desktop$ 
```
