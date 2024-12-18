# Crear y Formatear Particiones

## Objetivo 
Crear y formatear una nueva partición (Usar disco de práctica o máquina virtual).

## COMANDOS

```bash
vboxuser@uwuntu:~$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
loop0    7:0    0  74.3M  1 loop /snap/core22/1564
loop1    7:1    0     4K  1 loop /snap/bare/5
loop2    7:2    0 269.8M  1 loop /snap/firefox/4793
loop3    7:3    0  73.9M  1 loop /snap/core22/1722
loop4    7:4    0  10.7M  1 loop /snap/firmware-updater/127
loop5    7:5    0  11.1M  1 loop /snap/firmware-updater/147
loop6    7:6    0 505.1M  1 loop /snap/gnome-42-2204/176
loop7    7:7    0  91.7M  1 loop /snap/gtk-common-themes/1535
loop8    7:8    0  10.5M  1 loop /snap/snap-store/1173
loop9    7:9    0  44.3M  1 loop /snap/snapd/23258
loop10   7:10   0  38.8M  1 loop /snap/snapd/21759
loop11   7:11   0   500K  1 loop /snap/snapd-desktop-integration/178
loop12   7:12   0   568K  1 loop /snap/snapd-desktop-integration/253
sda      8:0    0    25G  0 disk 
├─sda1   8:1    0     1M  0 part 
└─sda2   8:2    0    25G  0 part /
sdb      8:16   0  19.3M  0 disk 
sr0     11:0    1  56.9M  0 rom  /media/vboxuser/VBox_GAs_7.1.4
vboxuser@uwuntu:~$    sudo fdisk -l
[sudo] password for vboxuser: 
Disk /dev/loop0: 74.27 MiB, 77881344 bytes, 152112 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop1: 4 KiB, 4096 bytes, 8 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop2: 269.77 MiB, 282873856 bytes, 552488 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop3: 73.87 MiB, 77459456 bytes, 151288 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop4: 10.72 MiB, 11239424 bytes, 21952 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop5: 11.11 MiB, 11649024 bytes, 22752 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop6: 505.09 MiB, 529625088 bytes, 1034424 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop7: 91.69 MiB, 96141312 bytes, 187776 sectors
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


Disk /dev/sdb: 19.3 MiB, 20232704 bytes, 39517 sectors
Disk model: VBOX HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop8: 10.54 MiB, 11051008 bytes, 21584 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop9: 44.3 MiB, 46448640 bytes, 90720 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop10: 38.83 MiB, 40714240 bytes, 79520 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop11: 500 KiB, 512000 bytes, 1000 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/loop12: 568 KiB, 581632 bytes, 1136 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
vboxuser@uwuntu:~$ ^C
vboxuser@uwuntu:~$ sudo fdisk /dev/sdb

Welcome to fdisk (util-linux 2.39.3).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS (MBR) disklabel with disk identifier 0x1fbc2a73.

Command (m for help):  sudo mkfs.ext4 /dev/sdX1
Created a new partition 1 of type 'Linux native' and of size 7.8 MiB.
Created a new partition 2 of type 'Linux swap' and of size 7.8 MiB.
Created a new partition 3 of type 'Whole disk' and of size 15.7 MiB.
Created a new Sun disklabel.

vboxuser@uwuntu:~/Desktop$ sudo mkfs.ext4 /dev/sdb
[sudo] password for vboxuser: 
mke2fs 1.47.0 (5-Feb-2023)
Creating filesystem with 4939 4k blocks and 4944 inodes

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (1024 blocks): done
Writing superblocks and filesystem accounting information: done


```