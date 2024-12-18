# Redirección de Entrada y Salida

## Objetivo
Usar redirección para guardar la salida de comandos en archivos.

## Intrucciones

### COMANDOS:

```bash
vboxuser@uwuntu:~/Desktop$ sudo ls -l > listado.txt
[sudo] password for vboxuser: 
vboxuser@uwuntu:~/Desktop$ sudo cat listado.txt
total 0
-rw-rw-r-- 1 vboxuser vboxuser 0 Dec 18 19:28 listado.txt
vboxuser@uwuntu:~/Desktop$ date >> listado.txt
vboxuser@uwuntu:~/Desktop$ cat listado.txt
total 0
-rw-rw-r-- 1 vboxuser vboxuser 0 Dec 18 19:28 listado.txt
Wed Dec 18 07:28:44 PM UTC 2024
vboxuser@uwuntu:~/Desktop$ 
```