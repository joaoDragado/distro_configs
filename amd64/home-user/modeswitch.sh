#!/bin/bash

usb_modeswitch -v 12d1 -p 1f1c -W -I -M 55534243123456780000000000000011062000000101000100000000000000

sleep 2s &

x-www-browser http://192.168.9.1/html/home.htm


exit
