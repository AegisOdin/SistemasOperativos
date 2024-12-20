# Explorar dispositivos de entrada

## Objetivo

**Identificar dispositivos como teclados, ratones y cámaras.**

## Intrucciones

### Ejecute `cat /proc/bus/input/devices` para listar los dispositivos de entrada.
```bash
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

I: Bus=0003 Vendor=80ee Product=0021 Version=0110
N: Name="VirtualBox USB Tablet"
P: Phys=usb-0000:00:06.0-1/input0
S: Sysfs=/devices/pci0000:00/0000:00:06.0/usb2/2-1/2-1:1.0/0003:80EE:0021.0001/input/input6
U: Uniq=
H: Handlers=mouse1 event5 js0 
B: PROP=0
B: EV=1f
B: KEY=1f0000 0 0 0 0
B: REL=1940
B: ABS=3
B: MSC=10

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
```

### Use `evtest` para monitorear eventos de dispositivos de entrada (requiere permisos de superusuario).
```bash
No device specified, trying to scan all of /dev/input/event*
Available devices:
/dev/input/event0:	Power Button
/dev/input/event1:	Sleep Button
/dev/input/event2:	AT Translated Set 2 keyboard
/dev/input/event3:	Video Bus
/dev/input/event4:	ImExPS/2 Generic Explorer Mouse
/dev/input/event5:	VirtualBox USB Tablet
/dev/input/event6:	VirtualBox mouse integration
Select the device event number [0-6]: 
```
Investigue los siguientes dispositivos:
Teclado
```bash
Input device name: "AT Translated Set 2 keyboard"
Supported events:
  Event type 0 (EV_SYN)
  Event type 1 (EV_KEY)
    Event code 1 (KEY_ESC)
    Event code 2 (KEY_1)
    Event code 3 (KEY_2)
    Event code 4 (KEY_3)
    Event code 5 (KEY_4)
    Event code 6 (KEY_5)
    Event code 7 (KEY_6)
    Event code 8 (KEY_7)
    Event code 9 (KEY_8)
    Event code 10 (KEY_9)
    Event code 11 (KEY_0)
    Event code 12 (KEY_MINUS)
    Event code 13 (KEY_EQUAL)
    Event code 14 (KEY_BACKSPACE)
    Event code 15 (KEY_TAB)
    Event code 16 (KEY_Q)
    Event code 17 (KEY_W)
    Event code 18 (KEY_E)
    Event code 19 (KEY_R)
    Event code 20 (KEY_T)
    Event code 21 (KEY_Y)
    Event code 22 (KEY_U)
    Event code 23 (KEY_I)
    Event code 24 (KEY_O)
    Event code 25 (KEY_P)
    Event code 26 (KEY_LEFTBRACE)
    Event code 27 (KEY_RIGHTBRACE)
    Event code 28 (KEY_ENTER)
    Event code 29 (KEY_LEFTCTRL)
    Event code 30 (KEY_A)
    Event code 31 (KEY_S)
    Event code 32 (KEY_D)
    Event code 33 (KEY_F)
    Event code 34 (KEY_G)
    Event code 35 (KEY_H)
    Event code 36 (KEY_J)
    Event code 37 (KEY_K)
    Event code 38 (KEY_L)
    Event code 39 (KEY_SEMICOLON)
    Event code 40 (KEY_APOSTROPHE)
    Event code 41 (KEY_GRAVE)
    Event code 42 (KEY_LEFTSHIFT)
    Event code 43 (KEY_BACKSLASH)
    Event code 44 (KEY_Z)
    Event code 45 (KEY_X)
    Event code 46 (KEY_C)
    Event code 47 (KEY_V)
    Event code 48 (KEY_B)
    Event code 49 (KEY_N)
    Event code 50 (KEY_M)
    Event code 51 (KEY_COMMA)
    Event code 52 (KEY_DOT)
    Event code 53 (KEY_SLASH)
    Event code 54 (KEY_RIGHTSHIFT)
    Event code 55 (KEY_KPASTERISK)
    Event code 56 (KEY_LEFTALT)
    Event code 57 (KEY_SPACE)
    Event code 58 (KEY_CAPSLOCK)
    Event code 59 (KEY_F1)
    Event code 60 (KEY_F2)
    Event code 61 (KEY_F3)
    Event code 62 (KEY_F4)
    Event code 63 (KEY_F5)
    Event code 64 (KEY_F6)
    Event code 65 (KEY_F7)
    Event code 66 (KEY_F8)
    Event code 67 (KEY_F9)
    Event code 68 (KEY_F10)
    Event code 69 (KEY_NUMLOCK)
    Event code 70 (KEY_SCROLLLOCK)
    Event code 71 (KEY_KP7)
    Event code 72 (KEY_KP8)
    Event code 73 (KEY_KP9)
    Event code 74 (KEY_KPMINUS)
    Event code 75 (KEY_KP4)
    Event code 76 (KEY_KP5)
    Event code 77 (KEY_KP6)
    Event code 78 (KEY_KPPLUS)
    Event code 79 (KEY_KP1)
    Event code 80 (KEY_KP2)
    Event code 81 (KEY_KP3)
    Event code 82 (KEY_KP0)
    Event code 83 (KEY_KPDOT)
    Event code 85 (KEY_ZENKAKUHANKAKU)
    Event code 86 (KEY_102ND)
    Event code 87 (KEY_F11)
    Event code 88 (KEY_F12)
    Event code 89 (KEY_RO)
    Event code 90 (KEY_KATAKANA)
    Event code 91 (KEY_HIRAGANA)
    Event code 92 (KEY_HENKAN)
    Event code 93 (KEY_KATAKANAHIRAGANA)
    Event code 94 (KEY_MUHENKAN)
    Event code 95 (KEY_KPJPCOMMA)
    Event code 96 (KEY_KPENTER)
    Event code 97 (KEY_RIGHTCTRL)
    Event code 98 (KEY_KPSLASH)
    Event code 99 (KEY_SYSRQ)
    Event code 100 (KEY_RIGHTALT)
    Event code 102 (KEY_HOME)
    Event code 103 (KEY_UP)
    Event code 104 (KEY_PAGEUP)
    Event code 105 (KEY_LEFT)
    Event code 106 (KEY_RIGHT)
    Event code 107 (KEY_END)
    Event code 108 (KEY_DOWN)
    Event code 109 (KEY_PAGEDOWN)
    Event code 110 (KEY_INSERT)
    Event code 111 (KEY_DELETE)
    Event code 112 (KEY_MACRO)
    Event code 113 (KEY_MUTE)
    Event code 114 (KEY_VOLUMEDOWN)
    Event code 115 (KEY_VOLUMEUP)
    Event code 116 (KEY_POWER)
    Event code 117 (KEY_KPEQUAL)
    Event code 118 (KEY_KPPLUSMINUS)
    Event code 119 (KEY_PAUSE)
    Event code 121 (KEY_KPCOMMA)
    Event code 122 (KEY_HANGUEL)
    Event code 123 (KEY_HANJA)
    Event code 124 (KEY_YEN)
    Event code 125 (KEY_LEFTMETA)
    Event code 126 (KEY_RIGHTMETA)
    Event code 127 (KEY_COMPOSE)
    Event code 128 (KEY_STOP)
    Event code 140 (KEY_CALC)
    Event code 142 (KEY_SLEEP)
    Event code 143 (KEY_WAKEUP)
    Event code 155 (KEY_MAIL)
    Event code 156 (KEY_BOOKMARKS)
    Event code 157 (KEY_COMPUTER)
    Event code 158 (KEY_BACK)
    Event code 159 (KEY_FORWARD)
    Event code 163 (KEY_NEXTSONG)
    Event code 164 (KEY_PLAYPAUSE)
    Event code 165 (KEY_PREVIOUSSONG)
    Event code 166 (KEY_STOPCD)
    Event code 172 (KEY_HOMEPAGE)
    Event code 173 (KEY_REFRESH)
    Event code 183 (KEY_F13)
    Event code 184 (KEY_F14)
    Event code 185 (KEY_F15)
    Event code 217 (KEY_SEARCH)
    Event code 226 (KEY_MEDIA)
  Event type 4 (EV_MSC)
    Event code 4 (MSC_SCAN)
  Event type 17 (EV_LED)
    Event code 0 (LED_NUML) state 0
    Event code 1 (LED_CAPSL) state 0
    Event code 2 (LED_SCROLLL) state 0
Key repeat handling:
  Repeat type 20 (EV_REP)
    Repeat code 0 (REP_DELAY)
      Value    250
    Repeat code 1 (REP_PERIOD)
      Value     33
```
Mouse
 **Esa parte no me dejo copiar y pegarla ya que no podia seleccionar con el mouse**
Controladores USB adicionales
```bash
Input device name: "VirtualBox USB Tablet"
Supported events:
  Event type 0 (EV_SYN)
  Event type 1 (EV_KEY)
    Event code 272 (BTN_LEFT)
    Event code 273 (BTN_RIGHT)
    Event code 274 (BTN_MIDDLE)
    Event code 275 (BTN_SIDE)
    Event code 276 (BTN_EXTRA)
  Event type 2 (EV_REL)
    Event code 6 (REL_HWHEEL)
    Event code 8 (REL_WHEEL)
    Event code 11 (REL_WHEEL_HI_RES)
    Event code 12 (REL_HWHEEL_HI_RES)
  Event type 3 (EV_ABS)
    Event code 0 (ABS_X)
      Value      0
      Min        0
      Max    32767
    Event code 1 (ABS_Y)
      Value      0
      Min        0
      Max    32767
  Event type 4 (EV_MSC)
    Event code 4 (MSC_SCAN)
Properties:
Testing ... (interrupt to exit)
```


## Conteste:

### 1. ¿Qué eventos genera cada dispositivo al interactuar con ellos?

#### **Teclado ("AT Translated Set 2 keyboard"):**
- **Eventos admitidos:**
  - **`EV_SYN`**: Eventos de sincronización para delimitar las acciones del teclado.
  - **`EV_KEY`**: Eventos clave, correspondientes a las teclas presionadas y liberadas.
    - Cada tecla tiene un código único, como `KEY_A` para la tecla "A".
  - **`EV_MSC`**: Eventos misceláneos como `MSC_SCAN`, que identifica el escaneo de hardware.
  - **`EV_LED`**: Manejo de indicadores LED como Num Lock, Caps Lock y Scroll Lock.
- **Eventos comunes al interactuar:**
  - Presionar una tecla genera un evento `EV_KEY` con el código de la tecla (`KEY_X`) y el estado (`1` para presionada).
  - Soltar una tecla genera el mismo evento pero con estado `0`.
  - Cambiar el estado de los LEDs (por ejemplo, activar Caps Lock) genera eventos `EV_LED`.

---

#### **Mouse ("ImExPS/2 Generic Explorer Mouse"):**
- **Eventos admitidos:**
  - **`EV_SYN`**: Eventos de sincronización.
  - **`EV_KEY`**: Botones del mouse (`BTN_LEFT`, `BTN_RIGHT`, etc.).
  - **`EV_REL`**: Movimientos relativos, como desplazamiento del cursor o del scroll.
    - `REL_X` y `REL_Y`: Movimiento horizontal y vertical.
    - `REL_WHEEL`: Movimiento de la rueda del mouse.
- **Eventos comunes al interactuar:**
  - Mover el mouse genera eventos `EV_REL` con valores en `REL_X` y `REL_Y`.
  - Hacer clic en los botones genera eventos `EV_KEY` con los códigos de los botones y sus estados (1 para presionado, 0 para liberado).
  - Usar el scroll genera eventos `REL_WHEEL`.

---

#### **Controladores USB ("VirtualBox USB Tablet"):**
- **Eventos admitidos:**
  - **`EV_SYN`**: Eventos de sincronización.
  - **`EV_KEY`**: Botones del mouse (`BTN_LEFT`, `BTN_RIGHT`, etc.).
  - **`EV_REL`**: Movimientos relativos como el desplazamiento horizontal o vertical.
  - **`EV_ABS`**: Movimientos absolutos, mapeados a una pantalla virtual.
    - `ABS_X` y `ABS_Y`: Coordenadas absolutas del dispositivo.
  - **`EV_MSC`**: Eventos misceláneos como `MSC_SCAN`.
- **Eventos comunes al interactuar:**
  - Arrastrar o mover el puntero genera eventos `EV_ABS` para las coordenadas absolutas.
  - Clics en los botones generan eventos `EV_KEY`.
  - Usar el scroll puede generar eventos `EV_REL`.

---

### 2. ¿Cómo se identifican los dispositivos en `/proc/bus/input/devices`?

Cada dispositivo de entrada se identifica mediante los siguientes campos:  

- **`I` (Información del Bus):**
  - Especifica el bus al que pertenece el dispositivo, como:
    - `0019`: Dispositivos de sistema (por ejemplo, botones de encendido/suspensión).
    - `0011`: Teclado PS/2.
    - `0003`: Dispositivo USB (por ejemplo, el "VirtualBox USB Tablet").
  - Incluye el identificador de fabricante (`Vendor`) y producto (`Product`), junto con la versión del dispositivo.

- **`N` (Nombre):**
  - Nombre descriptivo del dispositivo (por ejemplo, "AT Translated Set 2 keyboard").

- **`P` (Físico):**
  - Representa la ubicación física del dispositivo en el sistema (por ejemplo, `isa0060/serio0/input0` para el teclado).

- **`S` (Sysfs):**
  - Ruta al archivo de sistema asociado al dispositivo (por ejemplo, `/devices/platform/i8042/serio0/input/input2`).

- **`U` (Unique):**
  - Identificador único del dispositivo (puede estar vacío).

- **`H` (Handlers):**
  - Interfaces asociadas para interactuar con el dispositivo, como:
    - `kbd`: Para teclados.
    - `mouseX`: Para dispositivos apuntadores.
    - `eventX`: Para eventos asociados al dispositivo.

- **`B` (Bits de propiedades):**
  - Especifican las capacidades del dispositivo, como:
    - `EV_KEY`: Manejo de teclas.
    - `EV_REL` o `EV_ABS`: Movimientos relativos o absolutos.