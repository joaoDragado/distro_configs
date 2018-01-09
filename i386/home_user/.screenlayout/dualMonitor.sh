#!/bin/sh
xrandr --output DP3 --off --output DP2 --off --output DP1 --off --output HDMI3 --off --output HDMI2 --off --output HDMI1 --off --output LVDS1 --mode 1600x900 --pos 0x0 --rotate normal --output VGA1 --mode 1280x1024 --pos 1600x0 --rotate normal

#sleep 2s &
xrandr  --output LVDS1 --brightness 0.95 & 

sleep 2s &

#xrandr  --output VGA1 --brightness 0.18 --gamma 0.7:0.7:0.8
xrandr  --output VGA1 --brightness 0.18 --gamma 0.85:0.9:1.0
#xrandr  --output VGA1 --brightness 0.20 --gamma 0.85:0.9:1.0
#xrandr  --output VGA1 --brightness 0.23 --gamma 0.7:0.7:0.8
#xrandr  --output VGA1 --brightness 0.25 --gamma 0.5:0.5:0.6
