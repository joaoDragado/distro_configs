#!/bin/sh
xrandr --output DP3 --off --output DP2 --off --output DP1 --off --output HDMI3 --off --output HDMI2 --off --output HDMI1 --off --output LVDS1 --mode 1600x900 --pos 0x0 --rotate normal --output VGA1 --off

sleep 2s &

xrandr  --output LVDS1 --brightness 0.95
 
