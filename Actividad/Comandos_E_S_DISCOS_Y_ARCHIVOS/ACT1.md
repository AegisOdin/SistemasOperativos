# Montar y Desmontar Discos

## Objetivo

Aprender a montar y desmontar un dispositivo externo.

## Instrucciones

     lsblk
o

      fdisk -l
## Monta la memoria USB en un directorio, por ejemplo, `/mnt/usb`:      
** Solo puedo montar una unidad de disco porque no tengo una usb **

    ```bash
vboxuser@uwuntu:/$ sudo mount /dev/cdrom /mnt
mount: /mnt: WARNING: source write-protected, mounted read-only.
    ```
## Verifica que esté montado correctamente:

    ```bash
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           794M  1.6M  793M   1% /run
/dev/sda2        25G  5.8G   18G  25% /
tmpfs           3.9G     0  3.9G   0% /dev/shm
tmpfs           5.0M  8.0K  5.0M   1% /run/lock
tmpfs           794M  128K  794M   1% /run/user/1000
/dev/sr0         57M   57M     0 100% /mnt

    ```
## Copia un archivo desde tu directorio personal al dispositivo USB:

    ** No puedo copiar ya que se monto como read only**
    
## Desmonta la memoria USB:

     ```bash
     sudo umount \dev\sr0
     ```
