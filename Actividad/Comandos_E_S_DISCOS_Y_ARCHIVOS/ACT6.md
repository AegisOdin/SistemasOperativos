# Exploración de Dispositivos

## Objetivo

Identificar discos y particiones en el sistema.

## COMANDOS

```bash
vboxuser@uwuntu:~$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
loop0    7:0    0  74.3M  1 loop /snap/core22/1564
loop1    7:1    0     4K  1 loop /snap/bare/5
loop2    7:2    0  73.9M  1 loop /snap/core22/1722
loop3    7:3    0 269.8M  1 loop /snap/firefox/4793
loop4    7:4    0  10.7M  1 loop /snap/firmware-updater/127
loop5    7:5    0  11.1M  1 loop /snap/firmware-updater/147
loop6    7:6    0 505.1M  1 loop /snap/gnome-42-2204/176
loop7    7:7    0  91.7M  1 loop /snap/gtk-common-themes/1535
loop8    7:8    0  10.5M  1 loop /snap/snap-store/1173
loop9    7:9    0  38.8M  1 loop /snap/snapd/21759
loop10   7:10   0  44.3M  1 loop /snap/snapd/23258
loop11   7:11   0   500K  1 loop /snap/snapd-desktop-integration/178
loop12   7:12   0   568K  1 loop /snap/snapd-desktop-integration/253
sda      8:0    0    25G  0 disk 
├─sda1   8:1    0     1M  0 part 
└─sda2   8:2    0    25G  0 part /
sr0     11:0    1  56.9M  0 rom  /media/vboxuser/VBox_GAs_7.1.4
vboxuser@uwuntu:~$ du -sh /home/vboxuser/Desktop
12K	/home/vboxuser/Desktop
vboxuser@uwuntu:~$    df -h
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           794M  1.5M  793M   1% /run
/dev/sda2        25G  5.8G   18G  26% /
tmpfs           3.9G     0  3.9G   0% /dev/shm
tmpfs           5.0M  8.0K  5.0M   1% /run/lock
tmpfs           794M  140K  794M   1% /run/user/1000
/dev/sr0         57M   57M     0 100% /media/vboxuser/VBox_GAs_7.1.4
vboxuser@uwuntu:~$ 
```