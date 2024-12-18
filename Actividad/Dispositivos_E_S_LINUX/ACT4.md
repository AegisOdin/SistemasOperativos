# Examinar dispositivos de salida

## Objetivo

Entender cómo identificar dispositivos de salida como monitores y tarjetas de sonido.

## Intrucciones

### Use `xrandr` para listar las pantallas conectadas y sus resoluciones.

```bash
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
```


### Ejecute `aplay -l` para listar las tarjetas de sonido disponibles.

```bash
vboxuser@uwuntu:~$ sudo aplay -l
[sudo] password for vboxuser: 
**** List of PLAYBACK Hardware Devices ****
card 0: I82801AAICH [Intel 82801AA-ICH], device 0: Intel ICH [Intel 82801AA-ICH]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

### Use `lsof /dev/snd/*` para ver qué procesos están utilizando la tarjeta de sonido.
```bash
vboxuser@uwuntu:~$ lsof /dev/snd/*
COMMAND    PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
pipewire  2846 vboxuser   59u   CHR  116,1      0t0  412 /dev/snd/seq
pipewire  2846 vboxuser   60u   CHR  116,1      0t0  412 /dev/snd/seq
wireplumb 2850 vboxuser   35u   CHR  116,5      0t0  704 /dev/snd/controlC0
```

## Conteste:

### 1. **Salidas de video disponibles en el sistema**
Usando `xrandr`, se identificó una salida de video activa:

- **Salida:** `Virtual-1`  
  - **Resolución actual:** `1280x800` (establecida como principal).
  - **Resoluciones disponibles:**  
    ```
    1280x800, 1024x768, 800x600, 640x480, 320x240, 1152x720, 
    960x600, 928x580, 800x500, 768x480, 720x480, 640x400, 
    320x200, 1280x720, 1024x576, 864x486, 720x400, 640x350.
    ```

### 2. **Dispositivos de sonido detectados**
El comando `aplay -l` identificó un dispositivo de sonido:

- **Tarjeta:** `Intel 82801AA-ICH`  
  - **Dispositivo:** `Intel ICH`  
  - **Subdispositivos disponibles:** 1  
  - **Subdispositivo activo:** `subdevice #0`

### 3. **Procesos utilizando la tarjeta de sonido**
El comando `lsof /dev/snd/*` mostró que los siguientes procesos están utilizando el dispositivo de sonido:

1. **pipewire**  
   - **PID:** `2846`  
   - **Usuario:** `vboxuser`  
   - **Dispositivos utilizados:**  
     - `/dev/snd/seq` (dos instancias abiertas).

2. **wireplumber**  
   - **PID:** `2850`  
   - **Usuario:** `vboxuser`  
   - **Dispositivo utilizado:**  
     - `/dev/snd/controlC0`

