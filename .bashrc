#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return
#colorscript -r

alias ls='ls --color=auto'
alias gantinvidia='optimus-manager --switch nvidia'
alias warnamalam='redshift -l -90.0:90.0 -t 3400:3400 &'
alias bchrome='google-chrome-stable --enable-features=WebUIDarkMode --force-dark-mode'
#PS1='[\u@\h \W]\$ '
PS1='\W -> '



export PATH="$HOME/.local/bin:$PATH"
#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
#export SDKMAN_DIR="/home/ibnu/.sdkman"
#[[ -s "/home/ibnu/.sdkman/bin/sdkman-init.sh" ]] && source "/home/ibnu/.sdkman/bin/sdkman-init.sh"
