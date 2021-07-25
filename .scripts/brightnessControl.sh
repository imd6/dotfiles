#!/usr/bin/bash

# Brightness notification: dunst


icon_path=/usr/share/icons/Papirus/symbolic/status/
notify_id=817


function get_brightness {
    light -G
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
        light -A 5
        brightness_notification
        ;;
    down)
        light -U 5
        brightness_notification
	    ;;
    *)
        echo "Usage: $0 up | down "
        ;;
esac
