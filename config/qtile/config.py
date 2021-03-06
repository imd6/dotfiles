# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile.config import KeyChord, Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook, qtile
from libqtile.lazy import lazy
from typing import List  # noqa: F401

mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                             # My terminal of choice
myConfig = "/home/ibnu/.config/qtile/config.py"    # The Qtile config file location

keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod], "space",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod, "shift"], "c",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod], "p",
             #lazy.spawn("dmenu_run -p 'Run: '"),
             lazy.spawn("rofi -show drun -config ~/.config/rofi/themes/dt-dmenu.rasi -display-drun \"Run: \" -drun-display-format \"{name}\""),
             desc='Run Launcher'
             ),
         Key([mod], "q",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key(["control", "shift"], "e",
             lazy.spawn("emacsclient -c -a emacs"),
             desc='Doom Emacs'
             ),
         ### Switch focus to specific monitor (out of three)
         Key([mod], "w",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "e",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),
         Key([mod], "r",
             lazy.to_screen(2),
             desc='Keyboard focus to monitor 3'
             ),
         ### Switch focus of monitors
         Key([mod, "shift"], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod, "shift"], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),
         ### Treetab controls
         Key([mod, "control"], "k",
             lazy.layout.section_up(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "control"], "j",
             lazy.layout.section_down(),
             desc='Move down a section in treetab'
             ),
         ### Window controls
         Key([mod], "k",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "j",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "h",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod, "shift"], "m",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
	# Stack
          Key([mod], "Tab",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
	     ),
         Key([mod, "shift"], "space",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
         Key([mod, "control"], "Return",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
         ### Additional
         Key([mod, "shift"], "s",
             lazy.spawn("/home/ibnu/.scripts/dstartmenu"),
             desc='Launches Start menu script'
             ),
         Key([mod], "Print",
             lazy.spawn("scrot screen_%Y-%m-%d-%H-%M-%S.png -d 1 -e 'mv $f /home/ibnu/Pictures/Screenshot'"),
             desc='Screenshot Whole Display'
             ),
         Key([mod, "shift"], "Print",
             lazy.spawn("scrot window_%Y-%m-%d-%H-%M-%S.png -d 1 -u -e 'mv $f /home/ibnu/Pictures/Screenshot'"),
             desc='Screenshot Focused Window'
             ),
	 Key([], "XF86AudioMute",
	 lazy.spawn("/home/ibnu/.scripts/volumeControl.sh mute"),
	     desc='Toggle Audio'
	     ),
	 Key([], "XF86AudioLowerVolume",
	 lazy.spawn("/home/ibnu/.scripts/volumeControl.sh down"),
	     desc='Lower Volume'
	     ),
	 Key([], "XF86AudioRaiseVolume",
	 lazy.spawn("/home/ibnu/.scripts/volumeControl.sh up"),
	     desc='Raise volume'
	     ),
	 Key([], "XF86MonBrightnessUp",
	 lazy.spawn("/home/ibnu/.scripts/brightnessControl.sh up"),
	     desc='Raise Brightness'
	     ),
	 Key([], "XF86MonBrightnessDown",
	 lazy.spawn("/home/ibnu/.scripts/brightnessControl.sh down"),
	     desc='Raise Brightness'
	     ),
	 Key([], "XF86Sleep",
	 lazy.spawn("systemctl suspend"),
	     desc='Sleep/Suspend'
	     ),

]

group_names = [("WWW", {'layout': 'monadtall'}),
               ("DEV", {'layout': 'monadtall'}),
               ("DOC", {'layout': 'monadtall'}),
               ("MUS", {'layout': 'monadtall'}),
               ("GFX", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 2,
                "margin": 12,
                "border_focus": "fe8019",
                "border_normal": "282828"
                }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Max(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.Stack(num_stacks=2),
    #layout.TreeTab(
    #     font = "Ubuntu Mono",
    #     fontsize = 10,
    #     sections = ["FIRST", "SECOND"],
    #     section_fontsize = 11,
    #     bg_color = "141414",
    #     active_bg = "90C435",
    #     active_fg = "000000",
    #     inactive_bg = "384323",
    #     inactive_fg = "a0a0a0",
    #     padding_y = 5,
    #     section_top = 10,
    #     panel_width = 320
    #     ),
    # layout.Floating(**layout_theme)
]

colors = [["#282828", "#282828"], # dark bg
          ["#b8bb26", "#b8bb26"], # gruvbox green
          ["#ebdbb2", "#ebdbb2"], # fg
          ["#83a598", "#83a598"], # gruvbox blue
          ["#d3869b", "#d3869b"], # gruvbox purple
          ["#fabd2f", "#fabd2f"], # gruvbox yellow
          ["#fe8019", "#fe8019"], # gruvbox orange
          ["#8ec07c", "#8ec07c"], # gruvbox aqua
	  ["#E0585E", "#E0585E"], # gruvbox reddish
	  ["#fb4934", "#fb4934"], # gruvbox red
	  ["#504945", "#504945"]] # gruvbox dark

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="SF Pro Text Bold",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

# Mouse Callback Function
def open_rofi():
    qtile.cmd_spawn('rofi -show drun -config ~/.config/rofi/themes/dt-dmenu.rasi -display-drun \"Run: \" -drun-display-format \"{name}\"')
def open_htop():
    qtile.cmd_spawn('alacritty -e htop')
def open_powerkit():
    qtile.cmd_spawn('powerkit --config')
def open_nmtui():
    qtile.cmd_spawn('alacritty -e nmtui')
# End of Mouse Callback Function

def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/archicon-orange.png",
                       mouse_callbacks = {'Button1': open_rofi}
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
	    widget.GroupBox(
                       font = "SF Pro Text Bold",
                       fontsize = 10,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[6],
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[10],
                       highlight_method = "line",
                       this_current_screen_border = colors[1],
                       this_screen_border = colors [6],
                       other_current_screen_border = colors[2],
                       other_screen_border = colors[2],
                       foreground = colors[2],
                       background = colors[10]
                       ),
          #    widget.GroupBox(
          #             font = "SF Pro Text Semibold",
          #             fontsize = 10,
          #             margin_y = 3,
          #             margin_x = 0,
          #             padding_y = 5,
          #             padding_x = 3,
          #             borderwidth = 3,
          #             active = colors[6],
          #             inactive = colors[2],
          #             rounded = False,
          #             highlight_method = "block",
          #             foreground = colors[2],
          #             background = colors[10]
          #             ),
              widget.Sep(
                       linewidth = 0,
                       padding = 7,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[0],
                       background = colors[6],
                       padding = 1,
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                       foreground = colors[2],
                       background = colors[10],
                       padding = 5
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
              #Separation between left and right
              widget.Sep(
                       linewidth = 0,
                       padding = 0,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.TextBox(
                       text = "",
                       mouse_callbacks = {'Button1': open_nmtui },
                       padding = 5,
                       foreground = colors[10],
                       background = colors[6]
                       ),
              widget.Net(
                       interface = "wlp3s0",
                       format = '{down}  {up}',
                       foreground = colors[2],
                       background = colors[10],
                       padding = 5
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 8,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.TextBox(
                      text = "",
                       padding = 5,
                       foreground = colors[10],
                       background = colors[1]
                       ),
              widget.CPU(
                       foreground = colors[2],
                       background = colors[10],
	               format = '{load_percent}%',
                       update_interval = 1.0,
                       padding = 3
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 8,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.TextBox(
                      text = "",
                       foreground = colors[10],
                       background = colors[6],
                       padding = 5
                       ),
              widget.Memory(
                       format = '{MemUsed}MB',
                       foreground = colors[2],
                       background = colors[10],
                       mouse_callbacks = {'Button1': open_htop },
                       padding = 3
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 8,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 3,
                       foreground = colors[2],
                       background = colors[1]
                       ),
	      widget.Volume(
                        theme_path = '/home/ibnu/.config/qtile/icons/volume-icons',
                        mute_command = "pactl set-sink-mute 0 toggle",
                        foreground = colors[0],
                        background = colors[1],
                        padding = 1
                        ),
              widget.Volume(
                        mute_command = "pactl set-sink-mute 0 toggle",
                        foreground = colors[2],
                        background = colors[10],
                        padding = 3
                        ),
              widget.Sep(
                       linewidth = 0,
                       padding = 8,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 3,
                       foreground = colors[2],
                       background = colors[6]
                       ),
               widget.BatteryIcon(
                        battery = "BAT0",
                        mouse_callbacks = {'Button1': open_powerkit},
                        theme_path = '/home/ibnu/.config/qtile/icons/battery-icons',
                        padding = 0,
                        update_interval = 2,
                        background = colors[6]
                        ),
              widget.Sep(
                       linewidth = 0,
                       padding = 3,
                       foreground = colors[2],
                       background = colors[6]
                       ),
              widget.Battery(
                        battery = "BAT0",
                        charge_char = '',
                        discharge_char = "",
                        #format ='{char} {percent:2.0%} {hour:d}h:{min:02d}m',
                        format ='{percent:2.0%}',
                        foreground = colors[2],
                        padding = 3,
                        background = colors[10]
                        ),
              widget.Sep(
                       linewidth = 0,
                       padding = 8,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.TextBox(
                      text = "",
                       foreground = colors[10],
                       background = colors[1],
                       padding = 4
                       ),
	     widget.Systray(
                       background = colors[10],
                       padding = 2
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 2,
                       foreground = colors[2],
                       background = colors[10]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 8,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.TextBox(
                      text = "",
                       foreground = colors[10],
                       background = colors[6],
                       padding = 5
                       ),
              widget.Clock(
                       foreground = colors[2],
                       background = colors[10],
                       padding = 5,
                       format = "%a, %d %b %Y [ %H:%M ]"
                       ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                       # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20))]
      #      Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)), 
      #      Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='lxpolkit'),
    Match(wm_class='toolbar'),
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
#wmname = "LG3D"
wmname = "qtile"
