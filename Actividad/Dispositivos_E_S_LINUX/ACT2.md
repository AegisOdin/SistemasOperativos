# Verificar dispositivos de almacenamiento

## Objetivo

Aprender cómo identificar discos duros, particiones y su configuración.

## Intrucciones

Abra una terminal en su entorno Linux.
Ejecute los siguientes comandos y anote sus observaciones:

### Use el comando `fdisk -l` para listar todos los discos y particiones.
```bash
Disk /dev/loop0: 4 KiB, 4096 bytes, 8 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop1: 269.77 MiB, 282873856 bytes, 552488 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop2: 74.27 MiB, 77881344 bytes, 152112 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop3: 10.72 MiB, 11239424 bytes, 21952 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop4: 505.09 MiB, 529625088 bytes, 1034424 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop5: 91.69 MiB, 96141312 bytes, 187776 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop6: 10.54 MiB, 11051008 bytes, 21584 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop7: 38.83 MiB, 40714240 bytes, 79520 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/sda: 25 GiB, 26843545600 bytes, 52428800 sectors
Disk model: VBOX HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 74325FC8-8394-472E-B18F-11319C58F470

Device     Start      End  Sectors Size Type
/dev/sda1   2048     4095     2048   1M BIOS boot
/dev/sda2   4096 52426751 52422656  25G Linux filesystem


Disk /dev/loop8: 500 KiB, 512000 bytes, 1000 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```

### Utilice `blkid` para ver los identificadores UUID y los tipos de sistema de archivos.
```bash
/dev/sda2: UUID="bea16ab7-3d25-45cd-a1ea-200cc4e1991d" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="017c6ca7-ec81-49bf-8af9-9da9cfe6a367"
/dev/loop1: BLOCK_SIZE="131072" TYPE="squashfs"
/dev/loop8: BLOCK_SIZE="131072" TYPE="squashfs"
/dev/loop6: BLOCK_SIZE="131072" TYPE="squashfs"
/dev/loop4: BLOCK_SIZE="131072" TYPE="squashfs"
/dev/sr0: BLOCK_SIZE="2048" UUID="2024-10-10-17-52-15-90" LABEL="VBox_GAs_7.1.4" TYPE="iso9660"
/dev/loop2: BLOCK_SIZE="131072" TYPE="squashfs"
/dev/loop0: BLOCK_SIZE="131072" TYPE="squashfs"
/dev/loop7: BLOCK_SIZE="131072" TYPE="squashfs"
/dev/sda1: PARTUUID="bcd0a217-850e-4285-9028-3c01d886b887"
/dev/loop5: BLOCK_SIZE="131072" TYPE="squashfs"
/dev/loop3: BLOCK_SIZE="131072" TYPE="squashfs"
```

### Use `df -h` para listar los dispositivos montados y su espacio disponible.
```bash
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           794M  1.5M  793M   1% /run
/dev/sda2        25G  5.3G   18G  23% /
tmpfs           3.9G     0  3.9G   0% /dev/shm
tmpfs           5.0M  8.0K  5.0M   1% /run/lock
tmpfs           794M  124K  794M   1% /run/user/1000
/dev/sr0         57M   57M     0 100% /media/vboxuser/VBox_GAs_7.1.4
```

## Conteste:
### **1. ¿Qué dispositivos de almacenamiento están conectados a su sistema?**
Los dispositivos de almacenamiento detectados son:

1. **Dispositivos de bucle (`/dev/loopX`)**:
   - Usados para sistemas de archivos montados a partir de imágenes (como Snap).
   - Ejemplos: `/dev/loop0`, `/dev/loop1`, hasta `/dev/loop8`.

2. **Disco virtual principal (`/dev/sda`)**:
   - Tamaño: 25 GiB.
   - Modelo: `VBOX HARDDISK`.
   - Particiones:
     - `/dev/sda1`: 1 MiB, partición de arranque (BIOS boot).
     - `/dev/sda2`: 25 GiB, partición del sistema de archivos Linux.

3. **Unidad óptica virtual (`/dev/sr0`)**:
   - Contiene la imagen de las Guest Additions de VirtualBox (`VBox_GAs_7.1.4`).

---

### **2. ¿Qué particiones están montadas actualmente?**
Según la salida de `df -h`, las particiones montadas son:

1. **`/dev/sda2`**:
   - Montada en `/`.
   - Tamaño: 25 GiB, con 5.3 GiB usados y 18 GiB disponibles.

2. **`/dev/sr0`**:
   - Montada en `/media/vboxuser/VBox_GAs_7.1.4`.
   - Tamaño: 57 MiB (uso completo, 100%).

3. **Particiones temporales (`tmpfs`)**:
   - `tmpfs` en `/run`, `/dev/shm`, `/run/lock`, y `/run/user/1000`.

---

### **3. ¿Qué tipo de sistemas de archivos se usan en las particiones?**
Los sistemas de archivos detectados son:

1. **`ext4`**:
   - Usado en la partición principal `/dev/sda2`.

2. **`squashfs`**:
   - Usado en los dispositivos de bucle (`/dev/loopX`) para Snap.

3. **`iso9660`**:
   - Usado en la unidad óptica virtual `/dev/sr0`.

4. **`tmpfs`**:
   - Usado para sistemas de archivos temporales en memoria.