# Thinkpad Trackpoint speed configuration on Linux
change pointer speed of Trackpoint on Thinkpad

works well T60 with Ubuntu 13.10 and Ubuntu 14.04 LTS

## how to change
speed configration by write integer to file

`0` <- slower ------------ faster -> `250`

**ATTENTION** if write `0`, trackpoint does not move

## locate setting files

```sh
find /sys/devices/platform/i8042 -name name | xargs grep -Fl TrackPoint | sed 's/\/input\/input[0-9]*\/name$//'
```

> http://www.thinkwiki.org/wiki/How_to_configure_the_TrackPoint#Determining_TrackPoint_Path_ID

### depend Trackpad status
BIOS -> Config -> Keyboad and Mouse -> Trackpad

#### "Automatic"
enable Trackpad, default setting

    /sys/devices/platform/i8042/serio1/serio2/

- serio1: Trackpad
- serio**2**: **Trackpoint**

```console
$ echo 250 | sudo tee /sys/devices/platform/i8042/serio1/serio2/speed
$ echo 180 | sudo tee /sys/devices/platform/i8042/serio1/serio2/sensitivity
```

#### "Disabled"
disable Trackpad by BIOS

    /sys/devices/platform/i8042/serio1/

- serio**1**: **Trackpoint**

```console
$ echo 165 | sudo tee /sys/devices/platform/i8042/serio1/serio2/speed
$ echo 175 | sudo tee /sys/devices/platform/i8042/serio1/serio2/sensitivity
```

----

## c.f.

```console
# echo -n 120 > /sys/devices/platform/i8042/serio1/serio2/speed
# echo -n 250 > /sys/devices/platform/i8042/serio1/serio2/sensitivity
```

> [How to configure the TrackPoint - ThinkWiki](http://www.thinkwiki.org/wiki/How_to_configure_the_TrackPoint)

----

## APPENDIX

### log
write `255` to "speed" file for speed up on Ubuntu 13.10

#### search file

```sh
~$ ls -w 80 /sys/devices/platform/i8042/serio1
bind_mode    ext_dev  mindrag          rate         sensitivity  uevent
description  id       modalias         reach        skipback     upthresh
draghys      inertia  power            resetafter   speed        ztime
driver       input    press_to_select  resolution   subsystem
drvctl       jenks    protocol         resync_time  thresh
```
> speed

#### cat current speed

```sh
~$ cat /sys/devices/platform/i8042/serio1/speed
97 # default
```

#### write max speed

```sh
~$ echo 255 | sudo tee /sys/devices/platform/i8042/serio1/speed
255 # done
```
#### check file

```sh
~$ cat /sys/devices/platform/i8042/serio1/speed
255 # ok
```
