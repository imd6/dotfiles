##  _               _  __
## (_)_ __ ___   __| |/ /_
## | | '_ ` _ \ / _` | '_ \
## | | | | | | | (_| | (_) |
## |_|_| |_| |_|\__,_|\___/
##
# imd6 .zshrc file


#/usr/bin/colorscript -r
#./fm6000
neofetch
#rxfetch


# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Enable colors and change prompt:
autoload -U colors && colors

# History in cache directory:
HISTSIZE=1000
SAVEHIST=1000
HISTFILE=~/.cache/zsh/history


autoload -U compinit && compinit -u
zstyle ':completion:*' menu select
# Auto complete with case insenstivity
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'

zmodload zsh/complist
compinit
_comp_options+=(globdots)		# Include hidden files.

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

# vi mode
bindkey -v
export KEYTIMEOUT=1

# Use vim keys in tab complete menu:
bindkey -M menuselect 'h' vi-backward-char
bindkey -M menuselect 'k' vi-up-line-or-history
bindkey -M menuselect 'l' vi-forward-char
bindkey -M menuselect 'j' vi-down-line-or-history
bindkey -v '^?' backward-delete-char

# Change cursor shape for different vi modes.
function zle-keymap-select {
  if [[ ${KEYMAP} == vicmd ]] ||
     [[ $1 = 'block' ]]; then
    echo -ne '\e[1 q'
  elif [[ ${KEYMAP} == main ]] ||
       [[ ${KEYMAP} == viins ]] ||
       [[ ${KEYMAP} = '' ]] ||
       [[ $1 = 'beam' ]]; then
    echo -ne '\e[5 q'
  fi
}
zle -N zle-keymap-select
zle-line-init() {
    zle -K viins # initiate `vi insert` as keymap (can be removed if `bindkey -V` has been set elsewhere)
    echo -ne "\e[5 q"
}
zle -N zle-line-init
echo -ne '\e[5 q' # Use beam shape cursor on startup.
preexec() { echo -ne '\e[5 q' ;} # Use beam shape cursor for each new prompt.

#PATH
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.scripts:$PATH"

eval "$(starship init zsh)"


#Load zsh-syntax-highlighting; should be last.
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh 2>/dev/null



#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
#export SDKMAN_DIR="/home/ibnu/.sdkman"
#[[ -s "/home/ibnu/.sdkman/bin/sdkman-init.sh" ]] && source "/home/ibnu/.sdkman/bin/sdkman-init.sh"
