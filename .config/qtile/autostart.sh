#! /bin/bash 
setxkbmap gb &
lxsession &
nitrogen --restore &
picom --experimental-backends &
pipewire &
dunst &
nm-applet &
#mictray &
#powerkit &
#cbatticon -r 10 -l 20 -i symbolic &
#mate-power-manager &
#/usr/bin/emacs --daemon &
xset r rate 450 50 &
notify-send "Welcome home, $USER"
sleep 2s
volumeicon &
#redshift -l -5.115309:119.518395 -t 4000:4000 &
