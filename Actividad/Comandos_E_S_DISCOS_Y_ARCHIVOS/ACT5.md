# Permisos y Propiedades de Archivos

## Objetivo

Aprender a modificar permisos y propietarios de archivos.

## COMANDOS
```bash
vboxuser@uwuntu:~/Desktop$ touch privado.txt
vboxuser@uwuntu:~/Desktop$ chmod 600 privado.txt
vboxuser@uwuntu:~/Desktop$ sudo chown usuario privado.txt
[sudo] password for vboxuser: 
chown: invalid user: ‘usuario’
vboxuser@uwuntu:~/Desktop$ sudo chown other privado.txt
vboxuser@uwuntu:~/Desktop$ 
```