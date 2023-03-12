#!/usr/bin/bash

# Brightness notification: dunst


icon_path=/home/ibnu/.local/share/icons/Gruvbox-Material-Dark/symbolic/status/
notify_id=817
device=intel_backlight

function get_brightness {
    brightnessctl -m -d $device | awk -F, '{print substr($4, 0, length($4)-1)}'
}

function brightness_notification {
    brightness=`get_brightness`
    printf -v br_int %.0f "$brightness"
    echo $br_int
    bar=$(seq -s "─" $(($br_int / 5)) | sed 's/[0-9]//g')
    dunstify -r $notify_id -u low -i ${icon_path}display-brightness-symbolic.svg $bar
}

case $1 in
    up)
        brightnessctl s 5%+ -d $device
        brightness_notification
        ;;
    down)
        brightnessctl s 5%- -d $device
        brightness_notification
	    ;;
    *)
        echo "Usage: $0 up | down "
        ;;
esac
