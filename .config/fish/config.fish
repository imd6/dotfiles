#if status is-interactive
    # Commands to run in interactive sessions can go here
#end
#imd6 fish config

### ADDING TO THE PATH
# First line removes the path; second line sets it.  Without the first line,
# your path gets massive and fish becomes very slow.
set -e fish_user_paths
set -U fish_user_paths $HOME/.scripts $fish_user_paths

### EXPORT ###
set fish_greeting                                
#set TERM "xterm-256color"                         
set EDITOR "nvim"                 
set VISUAL "geany"      

### "bat" as manpager
set -x MANPAGER "sh -c 'col -bx | bat -l man -p'"



### SET EITHER DEFAULT EMACS MODE OR VI MODE ###
#function fish_user_key_bindings
#  # fish_default_key_bindings
#  fish_vi_key_bindings
#end
### END OF VI MODE ###

# Only run this in interactive shells
if status is-interactive

  # I'm trying to grow a neckbeard
  # fish_vi_key_bindings
  # Set the cursor shapes for the different vi modes.
  set fish_cursor_default     block      blink
  set fish_cursor_insert      line       blink
  set fish_cursor_replace_one underscore blink
  set fish_cursor_visual      block

  function fish_user_key_bindings
    # Execute this once per mode that emacs bindings should be used in
    fish_default_key_bindings -M insert
    fish_vi_key_bindings --no-erase insert
  end
end

# Emulates vim's cursor shape behavior
#set fish_cursor_default block
#set fish_cursor_insert line
#set fish_cursor_replace_one underscore
#set fish_cursor_visual block


### AUTOCOMPLETE AND HIGHLIGHT COLORS ###
set fish_color_normal '#ebdbb2'
set fish_color_autosuggestion '#83a598'
set fish_color_command '#b8bb26'
set fish_color_error '#fb4934'
set fish_color_param brcyan

#Aliases
alias gantinvidia='optimus-manager --switch nvidia'
alias warnamalam='redshift -l -90.0:90.0 -t 3400:3400 &'
alias baru="xhost + local:" # xhost +si:localuser:root
alias ..='cd ..'
alias mv='mv -i'
alias rm='rm -i'
alias pacup="sudo pacman -Syyu"

alias vim="nvim"
alias em="/usr/bin/emacs -nw"
alias emacs="emacsclient -c -a 'emacs'"
alias doomsync="~/.emacs.d/bin/doom sync"
alias doomdoctor="~/.emacs.d/bin/doom doctor"
alias doomupgrade="~/.emacs.d/bin/doom upgrade"
alias doompurge="~/.emacs.d/bin/doom purge"

alias la='exa -al --color=always --group-directories-first' # my preferred listing
alias ls='exa -a --color=always --group-directories-first'  # all files and dirs
alias ll='exa -l --color=always --group-directories-first'  # long format
alias lt='exa -aT --color=always --group-directories-first' # tree listing
alias l.='exa -a | egrep "^\."'

alias tobash="sudo chsh $USER -s /bin/bash && echo 'Now log out.'"
alias tozsh="sudo chsh $USER -s /bin/zsh && echo 'Now log out.'"

rxfetch

starship init fish | source
