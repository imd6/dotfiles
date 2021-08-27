#  _               _  __
# (_)_ __ ___   __| |/ /_
# | | '_ ` _ \ / _` | '_ \
# | | | | | | | (_| | (_) |
# |_|_| |_| |_|\__,_|\___/
#
# imd6 qtile config

# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
#import psutil
import json

from typing import List  # noqa: F401
from libqtile import qtile
from libqtile.config import (KeyChord,Key,Screen,Group,Drag,Click,Match,ScratchPad,DropDown,Match)
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
#from libqtile.lazy import lazy

from battery import bat_stat

mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                             # My terminal of choice
myConfig = "/home/ibnu/.config/qtile/config.py"    # The Qtile config file location

############# KEYBINDINGS ##############

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
        Key([mod, "shift"], "Return",
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
        Key([mod, "shift"], "b",
            lazy.spawn("google-chrome-stable --enable-features=WebUIDarkMode --force-dark-mode"),
            desc='Open Dark Theme Chrome'
            ),
    ### Stack
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
    ###KeyChord for application stuff
        KeyChord([mod],"a", [
             Key([], "e",
                 lazy.spawn("emacsclient -c -a 'emacs'"),
                 desc='Launch Emacs'
                 ),
             Key([], "c",
                 lazy.spawn("google-chrome-stable --enable-features=WebUIDarkMode --force-dark-mode"),
                 desc='Launch dmenu Start Menu'
                 )
             ]),

    ###KeyChord for dmenu scripts
        KeyChord([mod], "p", [
             Key([], "s",
                 lazy.spawn("/home/ibnu/.scripts/dstartmenu"),
                 desc='Launch dmenu Start Menu'
                 ),
             Key([], "m",
                 lazy.spawn("/home/ibnu/.scripts/dmtpfs"),
                 desc='Launch dmenu Start Menu'
                 )
             ]),
    ###KeyChord For Scratchpads
        KeyChord([mod], "s",[
            Key([], "m",
                  lazy.group["spd"].dropdown_toggle("music"),
                  desc='Open cmus on scratchpads'
                  ),
            Key([], "w",
                  lazy.group["spd"].dropdown_toggle("wp"),
                  desc='Open nitrogen on scratchpads'
                  ),
            Key([], "f",
                  lazy.group["spd"].dropdown_toggle("fm"),
                  desc='Open vifm on scratchpads'
                  )
             ]),
]

############# END OF KEYBINDINGS ##############


############# WORKSPACES AND SCRATCHPADS ##############

groups = [
    ScratchPad(
        "spd",
        [
            # define a drop down.
            # it is placed in the upper third of screen by default.
            DropDown(
                "music",
                myTerm + " --class dropdown -e cmus",
                height=0.6,
                on_focus_lost_hide=False,
                opacity=0.8,
                warp_pointer=False,
            ),
           DropDown(
                "fm",
                myTerm + " --class dropdown -e vifm",
                height=0.6,
                on_focus_lost_hide=False,
                opacity=0.8,
                warp_pointer=False,
            ),
           DropDown(
                "wp",
                "nitrogen",
                height=0.7,
                on_focus_lost_hide=False,
                opacity=0.9,
                warp_pointer=False,
            ),
        ],
    ),
    Group("1", label="I", layout="monadtall", matches =[Match(wm_class=["qutebrowser"]),
                                                          Match(wm_class=["Google-chrome"])
                                                          ]),
    Group("2", label="II", layout="monadtall", matches =[Match(wm_class=["Emacs"]),
                                                          Match(wm_class=["code"])
                                                          ]),
    Group("3", label="III", layout="monadtall", matches =[Match(wm_class=["libreoffice"])
                                                          ]),
    Group("4", label="IV", layout="monadtall", matches =[Match(wm_class=["mpv"])
                                                          ]),
    Group("5", label="V", layout="monadtall", matches =[Match(wm_class=["gimp"])
                                                          ]),
    Group("6", label="VI", layout="monadtall", matches =[Match()
                                                          ]),
    Group("7", label="VII", layout="monadtall", matches =[Match()
                                                          ]),


]

for i in range(len(groups)):
   keys.append(Key([mod], str((i)), lazy.group[str(i)].toscreen()))
   keys.append(Key([mod, "shift"], str((i)), lazy.window.togroup(str(i))))

# Old define Workspaces
#group_names = [("WWW", {'layout': 'monadtall'}),
#               ("DEV", {'layout': 'monadtall'}),
#               ("DOC", {'layout': 'monadtall'}),
#               ("MUS", {'layout': 'monadtall'}),
#               ("GFX", {'layout': 'monadtall'})]
#
#groups = [Group(name) for name, kwargs in group_names]
#
#
#for i, (name, kwargs) in enumerate(group_names, 1):
#    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
#    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

############# END OF WORKSPACES AND SCRATCHPADS ##############



############# LAYOUTS SETTINGS ##############

layout_theme = {"border_width": 2,
                "margin":8,
                "border_focus": "fe8019",
                "border_normal": "1D2021"
                }

layout_float = {"border_width": 1,
                "border_focus": "fb4934",
                "border_normal": "1D2021"
                }

layouts = [
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    #layout.MonadWide(**layout_theme),
    layout.Max(**layout_theme),
    #layout.Bsp(**layout_theme, fair=False),
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
    layout.Floating(**layout_float)
]

colors = [["#1D2021", "#1D2021"], # dark bg
          ["#b8bb26", "#b8bb26"], # gruvbox green
          ["#ebdbb2", "#ebdbb2"], # fg
          ["#83a598", "#83a598"], # gruvbox blue
          ["#d3869b", "#d3869b"], # gruvbox purple
          ["#fabd2f", "#fabd2f"], # gruvbox yellow
          ["#fe8019", "#fe8019"], # gruvbox orange
          ["#8ec07c", "#8ec07c"], # gruvbox aqua
          ["#E0585E", "#E0585E"], # gruvbox reddish
          ["#fb4934", "#fb4934"], # gruvbox red
          ["#504945", "#504945"], # gruvbox dark
          ["#98971a", "#98971a"]] # gruvbox green2

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

############# END OF LAYOUTS SETTINGS ##############

############# WIDGETS SETTINGS ##############
widget_defaults = dict(
    #font="JetBrainsMono Nerd Font Bold",
    font="Hack Nerd Font Bold",
    fontsize = 12,
    padding = 2,
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
            widget.Sep(
                linewidth = 0,
                padding = 2,
                foreground = colors[2],
                ),
            #widget.TextBox(
                #fontsize = 17,
                #text = "",
                #text = "",
                #text = "",
                #foreground = colors[6],
                #mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('/home/ibnu/.scripts/dstartmenu')},
                #padding = 6,
                #),
            widget.Image(
                filename = "~/.config/qtile/icons/archicon-orange.png",
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('/home/ibnu/.scripts/dstartmenu')}
                ),
            widget.TextBox(
                text = "|",
                foreground = colors[10],
                padding = 3
                ),
            widget.GroupBox(
                font = "Ubuntu Bold",
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
                this_current_screen_border = colors[6],
                this_screen_border = colors [10],
                other_current_screen_border = colors[6],
                other_screen_border = colors[10],
                foreground = colors[2],
                ),
            #widget.GroupBox(
                #font = "Ubuntu Bold",
                #fontsize = 10,
                #margin_y = 3,
                #margin_x = 0,
                #padding_y = 5,
                #padding_x = 3,
                #borderwidth = 3,
                #active = colors[6],
                #inactive = colors[2],
                #rounded = False,
                #this_current_screen_border = colors[10],
                #highlight_color = colors[2],
                #highlight_method = "block",
                #foreground = colors[2],
                #),
            widget.TextBox(
                text = "|",
                foreground = colors[10],
                padding = 0
                ),
            widget.CurrentLayoutIcon(
                custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                foreground = colors[2],
                padding = 1,
                scale = 0.7
                ),
            #widget.WindowCount(
                #foreground = colors[2],
                #padding = 3,
                #show_zero = True,
                #font = 'Ubuntu Bold'
                #),
            #widget.TextBox(
                #text = "|",
                #foreground = colors[10],
                #padding = 0
                #),
            widget.CurrentLayout(
                foreground = colors[2],
                padding = 3
                ),
            widget.TextBox(
                text = "|",
                foreground = colors[10],
                padding = 0
                ),
            widget.WindowName(
                foreground = colors[6],
                padding = 3
                ),
             
              #Separation between left and right

            widget.Systray(
                icon_size = 15,
                padding = 3
                ),
            widget.TextBox(
                text = "|",
                foreground = colors[10],
                padding = 3
                ),
            widget.Net(
                interface = "wlp3s0",
                format = ' {up}',
                foreground = colors[1],
                padding = 0
                ),
            widget.Net(
                interface = "wlp3s0",
                format = ' {down}',
                foreground = colors[1],
                padding = 3
                ),
            widget.TextBox(
                text = "|",
                foreground = colors[10],
                padding = 3
                ),
            widget.TextBox(
                fontsize = 12,
                text = "  cpu:",
                padding = 3,
                foreground = colors[7],
                ),
            widget.CPU(
                foreground = colors[7],
                format = '{load_percent}%',
                update_interval = 1.0,
                padding = 3
                ),
            widget.TextBox(
                text = "|",
                foreground = colors[10],
                padding = 3
                ),
            widget.TextBox(
                fontsize = 14,
                text = " ",
                foreground = colors[3],
                padding = 3
                ),
            widget.TextBox(
                text = "mem:",
                foreground = colors[3],
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                padding = 0
                ),
            widget.Memory(
                format = '{MemPercent}%',
                foreground = colors[3],
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                padding = 3
                ),
            widget.TextBox(
                text = "|",
                foreground = colors[10],
                padding = 3
                ),
            widget.TextBox(
                fontsize = 14,
                text = "",
                foreground = colors[4],
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
                padding = 5
                ),
            widget.TextBox(
                text = "vol:",
                foreground = colors[4],
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('pavucontrol')},
                padding = 3
                ),
            #widget.Volume(
                #theme_path = '/home/ibnu/.config/qtile/icons/volume-icons',
                #foreground = colors[4],
                #padding = 3
                #),
            widget.Volume(
                foreground = colors[4],
                padding = 3
                ),
            widget.TextBox(
                text = "|",
                foreground = colors[10],
                padding = 3
                ),
            widget.GenPollText(
                foreground=colors[5],
                fontsize=13.7,
                func=bat_stat,
                update_interval=3,
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('mate-power-preferences')},
                padding=5
                ),
            widget.Battery(
                #battery = "BAT0",
                #format ='{char} {percent:2.0%}',
                #format ='{char} {percent:2.0%} {hour:d}h:{min:02d}m',
                format ='batt: {percent:2.0%}',
                foreground = colors[5],
                padding = 3,
                update_interval=3,
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('mate-power-preferences')},
                ),
            widget.TextBox(
                text = "|",
                foreground = colors[10],
                padding = 3
                ),
            widget.TextBox(
                fontsize = 15,
                text = "",
                foreground = colors[8],
                padding = 5
                ),
            widget.Clock(
                foreground = colors[8],
                padding = 5,
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e calcurse')},
                format = "%a, %d %b %Y [ %H:%M ]"
                #format = "%b %d %Y [ %H:%M ]"
                ),
              ]
    return widgets_list

############# END OF WIDGETS SETTINGS ##############


############# LAYOUT AND WINDOW BEHAVIOUR #############

def init_widgets_screen():
    widgets_screen = init_widgets_list()
    return widgets_screen

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen(), opacity=1.0, size=20, background="#282828")),
            Screen(top=bar.Bar(widgets=init_widgets_screen(), opacity=1.0, size=20, background="#282828"))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen = init_widgets_screen()

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
cursor_warp = False
floating_layout = layout.Floating(**layout_float
   ,float_rules=[
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
    Match(title='Qalculate!'),  # Qalculate-gtk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

############# END OF LAYOUT AND WINDOW BEHAVIOUR #############

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
wmname = "LG3D"
