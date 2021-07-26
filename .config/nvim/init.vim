syntax on

set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set nu
set nowrap
set smartcase
set noswapfile
set incsearch

set colorcolumn=80
call plug#begin()

Plug 'morhetz/gruvbox'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline'
Plug 'ghifarit53/tokyonight-vim'

call plug#end()

colorscheme gruvbox
set background=dark
let g:airline_theme='tokyonight'
