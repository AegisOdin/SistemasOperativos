# Crear un script de resumen

## Objetivo

Automatizar la recopilación de información de dispositivos de entrada y salida.

## Intrucciones

### Cree un archivo llamado `dispositivos.sh` y agregue el siguiente contenido: ```bash #!/bin/bash echo "Dispositivos de bloque:" lsblk echo "Dispositivos USB:" lsusb echo "Dispositivos PCI:" lspci echo "Dispositivos de entrada:" cat /proc/bus/input/devices echo "Salidas de video:" xrandr echo "Tarjetas de sonido:" aplay -l ```
### Ejecute el script usando `bash dispositivos.sh`.
### Modifique el script para guardar la salida en un archivo llamado `resumendispositivos.txt`.

```bash
vboxuser@uwuntu:~/Desktop$ cat resumendispositivos.txt
Dispositivos de bloque:
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
loop9    7:9    0  44.3M  1 loop /snap/snapd/23258
loop10   7:10   0  73.9M  1 loop /snap/core22/1722
loop11   7:11   0   568K  1 loop /snap/snapd-desktop-integration/253
loop12   7:12   0  11.1M  1 loop /snap/firmware-updater/147
sda      8:0    0    25G  0 disk 
├─sda1   8:1    0     1M  0 part 
└─sda2   8:2    0    25G  0 part /
sr0     11:0    1  56.9M  0 rom  /media/vboxuser/VBox_GAs_7.1.4

Dispositivos USB:
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 002 Device 003: ID 80ee:0021 VirtualBox USB Tablet

Dispositivos PCI:
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

Dispositivos de entrada:
I: Bus=0019 Vendor=0000 Product=0001 Version=0000
N: Name="Power Button"
P: Phys=LNXPWRBN/button/input0
S: Sysfs=/devices/LNXSYSTM:00/LNXPWRBN:00/input/input0
U: Uniq=
H: Handlers=kbd event0 
B: PROP=0
B: EV=3
B: KEY=8000 10000000000000 0

I: Bus=0019 Vendor=0000 Product=0003 Version=0000
N: Name="Sleep Button"
P: Phys=LNXSLPBN/button/input0
S: Sysfs=/devices/LNXSYSTM:00/LNXSLPBN:00/input/input1
U: Uniq=
H: Handlers=kbd event1 
B: PROP=0
B: EV=3
B: KEY=4000 0 0

I: Bus=0011 Vendor=0001 Product=0001 Version=ab41
N: Name="AT Translated Set 2 keyboard"
P: Phys=isa0060/serio0/input0
S: Sysfs=/devices/platform/i8042/serio0/input/input2
U: Uniq=
H: Handlers=sysrq kbd event2 leds 
B: PROP=0
B: EV=120013
B: KEY=402000000 3803078f800d001 feffffdfffefffff fffffffffffffffe
B: MSC=10
B: LED=7

I: Bus=0019 Vendor=0000 Product=0006 Version=0000
N: Name="Video Bus"
P: Phys=LNXVIDEO/video/input0
S: Sysfs=/devices/LNXSYSTM:00/LNXSYBUS:00/PNP0A03:00/LNXVIDEO:00/input/input4
U: Uniq=
H: Handlers=kbd event3 
B: PROP=0
B: EV=3
B: KEY=3e000b00000000 0 0 0

I: Bus=0011 Vendor=0002 Product=0006 Version=0000
N: Name="ImExPS/2 Generic Explorer Mouse"
P: Phys=isa0060/serio1/input0
S: Sysfs=/devices/platform/i8042/serio1/input/input5
U: Uniq=
H: Handlers=mouse0 event4 
B: PROP=1
B: EV=7
B: KEY=1f0000 0 0 0 0
B: REL=143

I: Bus=0001 Vendor=80ee Product=cafe Version=0000
N: Name="VirtualBox mouse integration"
P: Phys=
S: Sysfs=/devices/pci0000:00/0000:00:04.0/input/input8
U: Uniq=
H: Handlers=mouse2 event6 js1 
B: PROP=0
B: EV=b
B: KEY=10000 0 0 0 0
B: ABS=3

I: Bus=0003 Vendor=80ee Product=0021 Version=0110
N: Name="VirtualBox USB Tablet"
P: Phys=usb-0000:00:06.0-1/input0
S: Sysfs=/devices/pci0000:00/0000:00:06.0/usb2/2-1/2-1:1.0/0003:80EE:0021.0002/input/input9
U: Uniq=
H: Handlers=mouse1 event5 js0 
B: PROP=0
B: EV=1f
B: KEY=1f0000 0 0 0 0
B: REL=1940
B: ABS=3
B: MSC=10


Salidas de video:
Screen 0: minimum 16 x 16, current 1280 x 800, maximum 32767 x 32767
Virtual-1 connected primary 1280x800+0+0 (normal left inverted right x axis y axis) 0mm x 0mm
   1280x800      59.81*+
   1024x768      59.92  
   800x600       59.86  
   640x480       59.38  
   320x240       59.52  
   1152x720      59.97  
   960x600       59.63  
   928x580       59.88  
   800x500       59.50  
   768x480       59.90  
   720x480       59.71  
   640x400       59.95  
   320x200       58.96  
   1280x720      59.86  
   1024x576      59.90  
   864x486       59.92  
   720x400       59.55  
   640x350       59.77  

Tarjetas de sonido:
**** List of PLAYBACK Hardware Devices ****
card 0: I82801AAICH [Intel 82801AA-ICH], device 0: Intel ICH [Intel 82801AA-ICH]
  Subdevices: 1/1
  Subdevice #0: subdevice #0

```

## Respuesta

### **Ventajas de usar un script para recopilar esta información**

1. **Automatización:**  
   Permite ejecutar múltiples comandos de forma secuencial sin intervención manual. Esto ahorra tiempo y reduce errores humanos.

2. **Consolidación de datos:**  
   Toda la información se recopila en un solo lugar (archivo o terminal), facilitando su análisis posterior.

3. **Reproducibilidad:**  
   Puede ejecutarse en diferentes máquinas o entornos para recopilar la misma información de manera consistente.

4. **Portabilidad:**  
   Es fácil de compartir con otros usuarios o equipos para que obtengan los mismos datos sin necesidad de explicar cada comando.

5. **Documentación:**  
   El script actúa como un registro de los pasos realizados, útil para auditorías o resolución de problemas.

6. **Salida personalizada:**  
   Es posible formatear la salida o redirigirla para integrarla con otras herramientas (logs, informes, etc.).

---

### **Cambios para personalizar el script**

#### 1. **Filtrar la información relevante**
   - Usar opciones específicas de los comandos para mostrar solo datos necesarios.  
     Por ejemplo, limitar `lsblk` a discos montados:  
     ```bash
     lsblk -o NAME,SIZE,MOUNTPOINT
     ```

#### 2. **Incluir fecha y hora en la salida**
   - Agregar un encabezado con la marca de tiempo para registrar cuándo se ejecutó el script:  
     ```bash
     echo "Reporte generado el: $(date)"
     ```

#### 3. **Permitir elegir la salida (pantalla o archivo)**
   - Usar variables o argumentos para decidir si se imprime en pantalla o se guarda en un archivo:  
     ```bash
     OUTPUT_FILE=${1:-"resumendispositivos.txt"}
     ```

#### 4. **Soporte para formatos específicos**
   - Guardar la salida en formatos como JSON o CSV para un análisis más estructurado:  
     ```bash
     echo "{\"Dispositivos de bloque\": $(lsblk -J)}" > $OUTPUT_FILE
     ```

#### 5. **Ampliar el alcance del script**
   - Incluir más información, como:
     - Procesos en ejecución: `ps aux`
     - Uso de memoria: `free -h`
     - Estado de red: `ip a`

#### 6. **Colores o resaltado para la terminal**
   - Mejorar la legibilidad en la terminal resaltando encabezados con colores:  
     ```bash
     echo -e "\033[1;34mDispositivos de bloque:\033[0m"
     ```

#### 7. **Añadir comprobaciones de errores**
   - Verificar si los comandos están instalados antes de ejecutarlos:  
     ```bash
     if ! command -v xrandr &> /dev/null; then
       echo "El comando xrandr no está disponible."
     fi
     ```


