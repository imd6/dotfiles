#Default Start
/usr/bin/colorscript -r
#./fm6000

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

#PATH
export PATH="$HOME/.local/bin:$PATH"

eval "$(starship init zsh)"
#Load zsh-syntax-highlighting; should be last.
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh 2>/dev/null

#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="/home/ibnu/.sdkman"
[[ -s "/home/ibnu/.sdkman/bin/sdkman-init.sh" ]] && source "/home/ibnu/.sdkman/bin/sdkman-init.sh"
