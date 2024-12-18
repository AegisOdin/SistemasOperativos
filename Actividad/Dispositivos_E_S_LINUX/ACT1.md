# **Listar dispositivos conectados**

## Objetivo
Conocer los dispositivos de entrada y salida conectados al sistema.

## Instrucciones
Abra una terminal en su entorno Linux.
Ejecute los siguientes comandos y anote sus observaciones:

### `lsblk`: Enumera los dispositivos de bloque.

```bash
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
loop0    7:0    0     4K  1 loop /snap/bare/5
loop1    7:1    0 269.8M  1 loop /snap/firefox/4793
loop2    7:2    0  74.3M  1 loop /snap/core22/1564
loop3    7:3    0  10.7M  1 loop /snap/firmware-updater/127
loop4    7:4    0 505.1M  1 loop /snap/gnome-42-2204/176
loop5    7:5    0  91.7M  1 loop /snap/gtk-common-themes/1535
loop6    7:6    0  10.5M  1 loop /snap/snap-store/1173
loop7    7:7    0  38.8M  1 loop /snap/snapd/21759
loop8    7:8    0   500K  1 loop /snap/snapd-desktop-integration/178
sda      8:0    0    25G  0 disk 
├─sda1   8:1    0     1M  0 part 
└─sda2   8:2    0    25G  0 part /
sr0     11:0    1  56.9M  0 rom  /media/vboxuser/VBox_GAs_7.1.4
```
---

### `lsusb`: Lista los dispositivos conectados a los puertos USB.
```bash
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 002 Device 002: ID 80ee:0021 VirtualBox USB Tablet
```
---

### `lspci`: Muestra los dispositivos conectados al bus PCI.
```bash
00:00.0 Host bridge: Intel Corporation 440FX - 82441FX PMC [Natoma] (rev 02)
00:01.0 ISA bridge: Intel Corporation 82371SB PIIX3 ISA [Natoma/Triton II]
00:01.1 IDE interface: Intel Corporation 82371AB/EB/MB PIIX4 IDE (rev 01)
00:02.0 VGA compatible controller: VMware SVGA II Adapter
00:03.0 Ethernet controller: Intel Corporation 82540EM Gigabit Ethernet Controller (rev 02)
00:04.0 System peripheral: InnoTek Systemberatung GmbH VirtualBox Guest Service
00:05.0 Multimedia audio controller: Intel Corporation 82801AA AC'97 Audio Controller (rev 01)
00:06.0 USB controller: Apple Inc. KeyLargo/Intrepid USB
00:07.0 Bridge: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 08)
00:0b.0 USB controller: Intel Corporation 82801FB/FBM/FR/FW/FRW (ICH6 Family) USB2 EHCI Controller
00:0d.0 SATA controller: Intel Corporation 82801HM/HEM (ICH8M/ICH8M-E) SATA Controller [AHCI mode] (rev 02)
```
---

### `dmesg | grep usb`: Muestra los mensajes del kernel relacionados con dispositivos USB.
```bash
[sudo] password for vboxuser: 
[    0.352568] usbcore: registered new interface driver usbfs
[    0.352568] usbcore: registered new interface driver hub
[    0.352568] usbcore: registered new device driver usb
[    0.449637] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.08
[    0.449642] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.449643] usb usb1: Product: EHCI Host Controller
[    0.449644] usb usb1: Manufacturer: Linux 6.8.0-51-generic ehci_hcd
[    0.449645] usb usb1: SerialNumber: 0000:00:0b.0
[    0.545872] usb usb2: New USB device found, idVendor=1d6b, idProduct=0001, bcdDevice= 6.08
[    0.545877] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.545878] usb usb2: Product: OHCI PCI host controller
[    0.545878] usb usb2: Manufacturer: Linux 6.8.0-51-generic ohci_hcd
[    0.545879] usb usb2: SerialNumber: 0000:00:06.0
[    0.840467] usb 2-1: new full-speed USB device number 2 using ohci-pci
[    1.241949] usb 2-1: New USB device found, idVendor=80ee, idProduct=0021, bcdDevice= 1.00
[    1.241954] usb 2-1: New USB device strings: Mfr=1, Product=3, SerialNumber=0
[    1.241955] usb 2-1: Product: USB Tablet
[    1.241956] usb 2-1: Manufacturer: VirtualBox
[    1.403539] usbcore: registered new interface driver usbhid
[    1.403542] usbhid: USB HID core driver
[    1.408764] input: VirtualBox USB Tablet as /devices/pci0000:00/0000:00:06.0/usb2/2-1/2-1:1.0/0003:80EE:0021.0001/input/input6
[    1.408823] hid-generic 0003:80EE:0021.0001: input,hidraw0: USB HID v1.10 Mouse [VirtualBox USB Tablet] on usb-0000:00:06.0-1/input0
```
---

## Conteste:
### **1. Tipos de dispositivos en la salida de `lsblk`:**
La salida de `lsblk` enumera dispositivos de bloque conectados al sistema, como discos duros, particiones y dispositivos de bucle (loop). En este caso:

- **`loopX`**: Dispositivos de bucle, utilizados para montar imágenes o archivos como si fueran discos físicos. Ejemplos en la salida: `/snap/firefox/4793`, `/snap/core22/1564`, etc.
- **`sda`**: Un disco físico virtual con dos particiones:
  - **`sda1`**: Una partición de 1 MB (probablemente utilizada para datos de arranque).
  - **`sda2`**: Una partición de 25 GB montada en el sistema de archivos raíz (`/`).
- **`sr0`**: Unidad óptica virtual (CD-ROM) que contiene la imagen de las Guest Additions (`VBox_GAs_7.1.4`).

---

### **2. Diferencia entre `lsusb` y `lspci`:**

- **`lsusb`**:
  - Enumera dispositivos conectados a los puertos USB.
  - Proporciona identificadores como `idVendor` (fabricante) e `idProduct` (producto).
  - Ejemplo: Un dispositivo USB tablet conectado con `idVendor=80ee` y `idProduct=0021`.

- **`lspci`**:
  - Enumera dispositivos conectados al bus PCI, como tarjetas de red, controladores SATA y tarjetas gráficas.
  - Incluye detalles sobre el tipo de dispositivo, fabricante y modelo.
  - Ejemplo: Controlador de red `Intel Corporation 82540EM Gigabit Ethernet Controller`.

**Resumen**:  
`lsusb` se enfoca exclusivamente en dispositivos USB, mientras que `lspci` muestra dispositivos conectados al bus PCI.

---

### **3. Información adicional proporcionada por `dmesg | grep usb`:**

El comando `dmesg | grep usb` muestra mensajes del kernel relacionados con dispositivos USB. En este caso, proporciona:

1. **Registro de eventos USB**:
   - Reconocimiento de nuevos dispositivos USB conectados.
   - Ejemplo: `"New USB device found, idVendor=80ee, idProduct=0021"`.

2. **Detalles técnicos del controlador**:
   - Indica el tipo de controlador USB en uso, como:
     - `EHCI Host Controller` (para USB 2.0).
     - `OHCI PCI host controller`.

3. **Cargado de controladores**:
   - Registro de los drivers cargados para dispositivos USB, como `usbhid` (USB Human Interface Device).

4. **Asignación de dispositivos**:
   - Asigna un dispositivo a un archivo en `/dev`. Ejemplo: Dispositivo de entrada para el tablet USB: 
     `"hid-generic 0003:80EE:0021.0001"`.

**Resumen**:  
`dmesg | grep usb` proporciona una vista detallada del proceso de detección, inicialización y configuración de dispositivos USB por parte del kernel.