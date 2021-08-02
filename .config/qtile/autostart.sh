#! /bin/bash 
#setxkbmap us &
lxsession &
nitrogen --restore &
picom --experimental-backends &
dunst &
nm-applet &
#powerkit &
#cbatticon -r 10 -l 20 -i symbolic &
mate-power-manager &
/usr/bin/emacs --daemon &
notify-send "Welcome home, $USER"
#redshift -l -5.115309:119.518395 -t 4000:4000 &
