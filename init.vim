"# vim aweseom, plugin repo for vim plugins https://vimawesome.com/{{{
"note: after tyring different plugins for a while you find that some of these plugins litterally have no documentation, while others have lots. So its best to check out everything that might solve your issue and maybe try all of them.  }}}

"
"# vundle plugin manager https://github.com/VundleVim/Vundle.vim{{{ 
" ok so i might switch to this pluggin manager at some point because
" vim-plug has several issues. however it does look like you cant use
" both at the same time. Or at least the stuff im supposed to have
" installed with both is not installing. So i might need to start with fresh
" rc file or fresh vim directory?? however it doesnt seem to be
" breaking anything. maybe i can leave it?
"

"set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" installing you complete me requires vundle
Plugin 'valloric/youcompleteme'





call vundle#end()            " required
filetype plugin indent on    " required
"}}}





""# Vim plug is a vim extension manager sorta >{{{
"https://github.com/junegunn/vim-plug
"to customize vim.
"read vim plug explanation.
"to install go here https://github.com/junegunn/vim-plug
"and follow the instructions for your system, I did it on windows and it was very painless to run a powershell script that got it done
"then you need to add 
"call plug#begin()
"call plug#end()
"to your vimrc somewhere and then add plugins between these two lines
"then Reload .vimrc and use "source % and then :PlugInstall in vim to install plugins.
"NOTE: recently encountered a bug where plugclean doesnt work, have to just
"delete the folder from .vim/plugged/
"
">  }}}
call plug#begin('~/.vim/plugged')
""https://vimawesome.com/plugin/vim-auto-save{{{
Plug '907th/vim-auto-save'
" }}}
"https://vimawesome.com/plugin/vim-colorschemes-sweeter-than-fiction{{{
Plug 'flazz/vim-colorschemes' 
" }}}
""https://vimawesome.com/plugin/the-nerd-commenter{{{
Plug 'scrooloose/nerdcommenter' 
" }}}
""https://vimawesome.com/plugin/vim-airline{{{
Plug 'bling/vim-airline'
" }}}
"" vim browser search{{{
"https://github.com/voldikss/vim-browser-search
"note you can find 3 others taht do similar here https://www.reddit.com/r/vim/comments/a4bpho/a_plugin_to_open_your_browser_and_search_for/
"this wont delete the text you searcehd which is lame, ill find a way to
"deal with that
Plug 'voldikss/vim-browser-search'
" }}}
""buffet buffer manager{{{
"" https://vimawesome.com/plugin/buffet-vim
"" this plugin will let you use an interactive menu to kill open buffers
"" with the :Bufferlist command
Plug 'sandeepcr529/buffet.vim'
  " }}}
"
""https://github.com/junegunn/fzf{{{
"Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
"Plug 'junegunn/fzf.vim'
" }}}
""https://vimawesome.com/plugin/nerdtree-red{{{
""Plug 'scrooloose/nerdtree'
""i uninstalled nerdtree because i didnt want to take the time to elanr to
""use its hotkeys, and its not better for basic file viewing
""https://vimawesome.com/plugin/vim-polyglot
"Plug 'sheerun/vim-polyglot'
" }}}
""name vim tabs{{{
"Plug 'gcmt/taboo.vim'
""use :Taboorename to rename the tab, then save the session to keep the
""changes. Hurray!! }}}
""# change name of tab manually{{{
"":set guitablabel=%{exists('t:mytablabel')?t:mytablabel\ :'' }}}}
"" bracey, alternative to emmet{{{
""https://vimawesome.com/plugin/bracey-vim
"Plug 'turbio/bracey.vim'
" }}}
""tabulous{{{
"" https://vimawesome.com/plugin/tabulous
"Plug 'webdevel/tabulous' " this plugin works great, but it doesnt save in the session which sucks. If it saved in session it would be perfect. I might look into that for the future.
""https://vimawesome.com/plugin/vim-tmux-navigator
""Plug 'christoomey/vim-tmux-navigator'
""this tmux-navigator plugin doesnt seem to work. Idk, the instructions were
""hazy. }}}
"" emmet, html autocompletion{{{
""https://vimawesome.com/plugin/emmet-vim
"Plug 'mattn/emmet-vim'
" }}}
""#vim surround {{{
""looked into this extension, looks cool but also has a learning curve? the docs suck, dont want to deal with it rn, but later }}}
""20. there is an html helper called sparkup that adds the autocomplettion and other cool things you have by default in vs code. there are probably more need to research and implement sometime{{{

" }}}
""22. add the git blame stuff from vs code??? maybe?{{{
"
" }}}
"" coc conquer of completion{{{
""https://vimawesome.com/plugin/coc-nvim
"" at first this didnt work, then i found out i followed the tutorial for
"" vim not nvim. then it still wasnt working so i looked into vim plug and
"" it said i should run plugupdate, and that did the trick
"" there was an issue with coc service not starting, but I found out you
"" need to install a language service like such as :CocInstall coc-json then
"" everything works!!
"" coc extensions https://github.com/neoclide/coc.nvim/wiki/Using-coc-extensions
"" NOTE: after isntalling it, it should have worked according to the tutorials
"" i saw, but it didnt at all, merely stopped throwing errors. 
"" also things slowed to the point of not being useable, i tried to get it
"" working on wsl reall fast but it turns out i have a tone of really useful
"" stuff in my rc that makes vim worth useing. so its back to the drawing
"" board, i deleted it so my shit would work again and maybe ill try to use it
"" with a separate rc file, but I dont want my normal shit to get fucked up.
"" idk ill figure something out. 
""Plug 'neoclide/coc.nvim', {'branch': 'release'}
" }}}
" you complete me{{{
" https://github.com/ycm-core/YouCompleteMe#linux-64-bit 
" Plug 'valloric/youcompleteme'
"getting an error with python3. but i have a high enough version installed so idk what it is. ill have to come back to this
"}}}
"IndexedSearch.vim{{{
"https://vimawesome.com/plugin/indexedsearch
Plug 'henrik/vim-indexed-search'
"ok this seems to work quite well, even though it looks like it uses up the whole status bar which is less ideal. 
"ill keep using and report as i go
"wait it also shows the search info in the vim aiplane thing, which is hella
"cool, ok complaints gone for now
"}}}
call plug#end()

let mapleader = " "
"nnoremap <silent> <leader>c} V}:call NERDComment('x', 'toggle')<CR>
" map keys to use vim browser search plugin{{{
nmap <silent> <Leader>g <Plug>SearchNormal
vmap <silent> <Leader>g <Plug>SearchVisual
" }}}

"change hotkey for using emmet
let g:user_emmet_leader_key='<A-,>'
let g:airline#extensions#tabline#enabled = 1 "enable vim-airline
"NERDTree hotkeys{{{
"nnoremap <leader>n :NERDTreeFocus<CR>
"nnoremap <C-n> :NERDTree<CR>
"nnoremap <C-t> :NERDTreeToggle<CR>
"nnoremap <C-f> :NERDTreeFind<CR> }}}
"autosave options{{{
let g:auto_save = 1  " enable AutoSave on Vim startup
let g:auto_save_events = ["InsertLeave", "TextChanged"]
let g:auto_save_write_all_buffers = 1  " write all open buffers as if you would use :wa
"let g:auto_save_postsave_hook = 'mks! kubuntuSession' " should save the session anytime it is updated????
" }}}
" session options{{{
set sessionoptions+=tabpages,globals,winsize,unix,slash	" allows the seesion to save the tab names you set, unix and slash allow sessions to work in windows and linux? globals is supposed to put global settings into the session i think}}}
"Indention Options{{{
"
" vim html autoformating{{{
""https://stackoverflow.com/questions/815548/how-do-i-tidy-up-an-html-files-indentation-in-vi
""it says to use these 
"":filetype indent on
"":set filetype=html # abbrev -  :set ft=html
""# vim fixing indentation https://vim.fandom.com/wiki/Fix_indentation
""gg=G will do the vs code format document trick, so fucking useful!!!
""= will fix for current line }}}

set smartindent " abbrev -  :set si
"set autoindent "New lines inherit the indentation of previous lines.
set expandtab "Convert tabs to spaces.
"set ai " short for set auto indent i think https://www.serverwatch.com/guides/automatic-indenting-vim/
filetype plugin indent on " Enable indentation rules that are file-type specific. Here indent is seperate from on, you can also put plugin to detect filetype plugin info. 
set shiftround "When shifting lines, round the indentation to the nearest multiple of “shiftwidth.”
set shiftwidth=2 "When shifting, indent using four spaces.
set smarttab "Insert “tabstop” number of spaces when the “tab” key is pressed.
set tabstop=1 "indents in tabs by number you set
set breakindent " makes it so lines that wrap will also indent. hella cool, there were like 5 other answered that included this but did hella extra shit and i was so confused but just this is what i wanted
"
" }}}

set guioptions-=e

"Search Options{{{
set hlsearch "Enable search highlighting.
set ignorecase "Ignore case when searching.
set incsearch "Incremental search that shows partial matches.
set smartcase "Automatically switch search to case-sensitive when search query contains an uppercase letter.
"should make it so i can serach highlighted text with two forward slashes https://vim.fandom.com/wiki/Search_for_visually_selected_text
vnoremap // y/\V<C-R>=escape(@",'/\')<CR><CR>  }}}
"Performance Options{{{
set complete-=i "Limit the files searched for auto-completes.
set lazyredraw "Don’t update screen during macro and script execution. }}}
"Text Rendering Options{{{
set display+=lastline "Always try to show a paragraph’s last line.
set encoding=utf-8 "Use an encoding that supports unicode.
set scrolloff=1 "The number of screen lines to keep above and below the cursor.
set sidescrolloff=5 "The number of screen columns to keep to the left and right of the cursor.
"syntax enable "Enable syntax highlighting. }}}
"User Interface Options{{{
"set laststatus=2 "Always display the status bar.
set ruler "Always show cursor position.
set wildmenu "Display command line’s tab complete options as a menu.
set tabpagemax=50 "Maximum number of tab pages that can be opened from the command line.
colorscheme gruvbox "Change color scheme.
set cursorline cursorcolumn "Highlight the line currently under cursor.
" Enable CursorLine
"set cursorline

"the following lines came from https://stackoverflow.com/questions/6488683/how-to-change-the-cursor-between-normal-and-insert-modes-in-vim
autocmd InsertEnter * set cul cuc
"Change Color when entering Insert Mode
autocmd InsertEnter * highlight  CursorLine ctermbg=Green ctermfg=DarkRed
autocmd InsertLeave * set nocul nocuc


set number "Show line numbers on the sidebar.
"set relativenumber "Show line number on the current line and relative numbers on all other lines.
set noerrorbells "Disable beep on errors.
set visualbell "Flash the screen instead of beeping on errors.
set mouse=a "Enable mouse for scrolling and resizing.
set title "Set the window’s title, reflecting the file currently being edited.
set background=dark "Use colors that suit a dark background. }}}
"Miscellaneous Options{{{
"set autoread "Automatically re-read files if modified outside Vim.{{{
"au CursorHold * checktime " taken from https://superuser.com/questions/181377/auto-reloading-a-file-in-vim-as-soon-as-it-changes-on-disk
" this is suppoed to help files autoread cause it doesnt always workforme
" update, this line actually works, hazza!
set autoread | au CursorHold * checktime | call feedkeys("lh")
"# to force a refresh of a file in vim that has been changed by another file{{{
"use the :e which means edit. 
"or use :e! which means force edit. }}} }}}
set backspace=indent,eol,start "Allow backspacing over indention, line breaks and insertion start.
"set backupdir=~/.cache/vim "Directory to store backup files.
set confirm "Display a confirmation dialog when closing an unsaved file.
set dir=~/.cache/vim "Directory to store swap files.
set formatoptions+=j "Delete comment characters when joining lines.
set hidden "Hide files in the background instead of closing them.
set history=1000 "Increase the undo limit.
set nomodeline "Ignore file’s mode lines; use vimrc configurations instead.
set noswapfile "Disable swap files.
set nrformats-=octal "Interpret octal as decimal when incrementing numbers.
set shell "The shell used to execute commands.
set spell "Enable spellchecking.
set complete+=kspell " use CN or CP to autocomplete words while typeing in insert mode 
set wildignore+=.pyc,.swp "Ignore files matching these patterns when opening files based on a glob pattern.
" shortcut keys to move between 
set linebreak "Avoid wrapping a line in the middle of a word.
set wrap "Enable line wrapping.
set whichwrap+=h,l " make it so you move to the next line with h and l when you are at the end or beginning of the line.
:set nrformats+=alpha " this should make it so i can use ctrl+a to make alphabetical lists  }}}
" make it so j and k move through wrapped lines automatically, this is super{{{
" duper great and I love it.
nnoremap j gj
nnoremap k gk
vnoremap j gj
vnoremap k gk
nnoremap <Down> gj
nnoremap <Up> gk
vnoremap <Down> gj
vnoremap <Up> gk
inoremap <Down> <C-o>gj
inoremap <Up> <C-o>gk

" escape to normal mode please god"{{{
" folks talking about differen popular methods of mapping escape to other keys
" https://vi.stackexchange.com/questions/300/other-ways-to-exit-insert-mode-besides-escape
"I wanna try using two letters on home row, but not anything that involves using keys that wont be on other vim setups.

inoremap ;; <ESC>
vnoremap ;; <ESC>
nnoremap ;; <ESC>
tnoremap ;; <ESC>

" also maping caplock to escape or whatever.... i could do that
"
":map! ;l ^[
":vmap ;l ^[

"noremap <A-e> <C-\><C-n>
"noremap! <A-e> <C-\><C-n>

"}}}
"
"following line sends escape on control c, becuase control c does not{{{
"send insert mode leave by default
ino <C-C> <Esc> 
"inoremap <Left> <C-o>gh
"inoremap <Right> <C-o>gl }}}
" make vim use the system clipboard and visa versa{{{
set clipboard+=unnamedplus 
nmap <silent> <A-k> :wincmd k<CR>
nmap <silent> <A-j> :wincmd j<CR>
nmap <silent> <A-h> :wincmd h<CR>
nmap <silent> <A-l> :wincmd l<CR>
" these inoremaps dont seem to work, idk why. something must be
" conflicting?
"inoremap <silent> <A-k> :wincmd k<CR>
"inoremap <silent> <A-j> :wincmd j<CR>
"inoremap <silent> <A-h> :wincmd h<CR>
"inoremap <silent> <A-l> :wincmd l<CR>
"nmap gx :silent execute "!xdg-open " . shellescape("<cWORD>")<CR>
"nmap gx :!xdg-open <c-r><c-a>
nnoremap <C-p> :GFiles<Cr>
" }}}
" tnoremap maps the stupid built in vim terminal so it can be easily exited.{{{
tnoremap <silent> <Esc> <C-\><C-n>
tnoremap <silent> <A-k> <C-\><C-n> :wincmd k<CR>
tnoremap <silent> <A-j> <C-\><C-n> :wincmd j<CR>
tnoremap <silent> <A-h> <C-\><C-n> :wincmd h<CR>
tnoremap <silent> <A-l> <C-\><C-n> :wincmd l<CR>
" }}}
" normal movements in insert or command mode, move normally by using Ctrl{{{
" these never worked boooooo, really want them too but for now will have to
" turn them off
"inoremap <C-h> <Left>
"inoremap <C-j> <Down>
"inoremap <C-k> <Up>
"inoremap <C-l> <Right>
"inoremap <C-h> <C-o>h
"inoremap <C-j> <C-o>j
"inoremap <C-k> <C-o>k
"inoremap <C-l> <C-o>l }}}
"Code Folding Options{{{
"folding https://vim.fandom.com/wiki/Folding
"folding 
"also found this tutorial useful https://www.linux.com/training-tutorials/vim-tips-folding-fun/#:~:text=zf%23j%20creates%20a%20fold,cursor%20to%20the%20previous%20fold.
"zf#j creates a fold from the cursor down # lines.
"zf/string creates a fold from the cursor to string.
"zj moves the cursor to the next fold.
"zk moves the cursor to the previous fold.
"zo opens a fold at the cursor.
"zO opens all folds at the cursor.
"zm increases the foldlevel by one.
"zM closes all open folds.
"zr decreases the foldlevel by one.
"zR decreases the foldlevel to zero — all folds will be open.
"zd deletes the fold at the cursor.
"zE deletes all folds.
"[z move to start of open fold.
"]z move to end of open fold.
"allows you to collaps lines into one line and you can open them later. 
"super useful, gonna use it all the time
"recently switched to indented folds, which you can toggle, i think its a more ellegant way of folding because its in the file, not just saved in vim. 
"nOTE: found out you cant put links in the indented folds or it folds them all together. Not sure why. Will try to figure it out. which hell sucks for my workflow, maybe i should research that
"but idk how well it will work with things that are not md files.
"use the foldmethod marker to dfine fold areas
"i tried the indent fold method and it doesnt work w
"this guy shows you can use the vim diff command to see how two files are open which is hella based https://www.youtube.com/watch?v=ovRqGybIg1Q
" fold method syntax uses the syntax of whatever language you are using.
" fold method diff is just a part of the vim diff tool. run vim -d file1 file2
" to compare differences, unchanged text will be folded
set foldmethod=marker "Fold based on indention levels. favorite so far by wide margin
"ok, im fucking mad, foldmethod marker doesnt fucking work with sessions?
"it does work with a single file i opened.
"you have you turn it on buffer by buffer, idk how to get it to work ugh!
"UPDATE: if you set the marker buffer by buffer then save the session it
"works. Holly fuck, I might just switch to emacs cause it bet there are fewer
"bugs lol
"set foldnestmax=0 ""Sets the maximum nesting of folds for the "indent" and "syntax"
	"methods.  This avoids that too many folds will be created.  Using more
	"than 20 doesn't work, because the internal limit is 20.
"set foldenable "Open all folds if not set.
set foldlevel=0 " zero will close all folds.  Higher numbers will
	"close fewer folds." these lines are supposed to automatically save the folds you make in your, might edit this later but rn i want everything closed when I open file. 
" vim files, 
" ok the following two lines dont work i think because nvim handles views
" differently than vim. might have to look into this more later, this folding
" business is turning out to be way to involved, this iis a test to see how
" fark
"autocmd BufWinLeave *.* mkview 
"autocmd BufWinEnter *.* silent loadview
" the following line is taken from https://superuser.com/questions/581572/insert-single-character-in-vim#:~:text=In%20Vim%20(7.2)%2C%20there,return%20you%20to%20normal%20mode.
"nnoremap <C-i> i_<Esc>r 
" it only inserts a space, which i wanted to choose the character i put in
" real time, might have to keep looking
" open folds on double click{{{
noremap <2-LeftMouse> za 
"}}}
" syntax highlighting not working when i use folds sometimes this article{{{
" suggested some stuff that did not help https://www.reddit.com/r/vim/comments/rhcpg/problem_with_syntax_highlighting_after_folds/ }}}
"

" }}}
"# create ordered list. https://stackoverflow.com/questions/4224410/macro-for-making-numbered-lists-in-vim{{{
"there are at least two cool ways to do this
"one use a macro that reads the previous line and then there is a key to increment numbers lol
"the others with visual block
"note, the block method seems better for scale, probably would recomend that 
"
"}}}
"# vim fzf {{{
"tutorial https://levelup.gitconnected.com/improving-vim-workflow-with-fzf-3f8bedaca1b2
"the main take away from this tutorial is the :GFiles command, which lets you search every file not in any gitignore, and when you hit enter it opens it. Could be very very cool if tied to a hotkey.
"the guy suggest this "nnoremap <C-p> :GFiles<Cr>"
"another tutorial https://sidneyliebrand.medium.com/how-fzf-and-ripgrep-improved-my-workflow-61c7ca212861
"# ripgrep https://blog.burntsushi.net/ripgrep/
"great article explaining pros and cons of rg. Its faster.
"It looks very cool, probably worth using, however, ill wait till i learn more bash stuff }}}
"# spell checking https://www.linux.com/training-tutorials/using-spell-checking-vim/{{{
"put 'set spell'
"use brackets then s to move forward and backward to different misspelled words which are underlined
"use 'z=' to open a word list
"'zg' to add word to dictionary
"'zw' to mark word as incorrect
"* also put 'set complete+=kspell' and use with crtl+n or p to get word auto complete in insert mode. Hella cool }}}
"# move tabs{{{
"https://vi.stackexchange.com/questions/3812/how-do-i-reorder-open-tabs
":tabmove 0
"move tab to the first position }}}
"# using vim in vscode {{{
"its not clear off the bat but to edit your vs code settings.json go...
"1. Ctrl/cmd-shift-p
"2. Type settings.json.
"3. Select Preferences: open settings.json.
"then you can eddit settings for the vim extension. 
"there is a section in the vim extention doc that shows an example of some settings you can edit. paste that into the settings.json to get started. 
"you have to restart after changeing the settings to get them to work, sometimes, not sure if its all the time
"i have not tried to use the vscode neovim extension yet.

"# vscode workspaces
"so you can use vscode to switch between workspaces with control-r. 
"it works ok, could be a lot faster. 
"ill keep it for now, but just because it takes like 5 seconds to switch between workspaces, i suspect ill switch to vim.
"also i had to make a couple of updates to the settings.json to get it to work with the vim extension

"# vscode vim vs neo vim https://galenwong.github.io/blog/2021-03-22-vscode-neovim-vs-vscodevim/
"basically neovim seems way better, ill switch but not right now.


" }}}
"# vim adventures https://vim-adventures.com/uu{{{
"cool vim teaching game you can play }}}
"# the vim buffer{{{
"the vim buffer is basically the file you are curently looking at. 
"use :b filename to switch to any buffer that is currently open 
"# i suspect that there are too many vim buffers open in my session thats why its slow.  }}}
"chaining commands in vim{{{
"#  https://vim.fandom.com/wiki/Multiple_commands_at_once
"you can chain commands with the | operator
"for example :%s/htm/html/c | %s/JPEG/jpg/c | %s/GIF/gif/c }}}
"# how to make movement keys work inside wrapped lines https://vim.fandom.com/wiki/Move_cursor_by_display_lines_when_wrapping{{{
"there are some intricacies to this so ill deal with it later }}}
"# vimrc on windows https://superuser.com/questions/86246/where-should-the-vimrc-file-be-located-on-windows-7{{{
"in vim use ':echo $HOME' to find your vim home directory, it should be C:users/yourusername
"make sure you use the command line to create your _vimrc_(underscore vimrc. for some reason the syntax highlight is all fucked up with just a single underscore) file, otherwise it didnt work for me the first time i did it?
"test it by adding "set number" to it, then save and reopen your vim file, it should have line numbers.
"* :source % will reload the vimrc file after you have made changes to it so you dont have to quite and re open, note only for the current file. 
"* to reload all buffers use this command :execute 'bufdo so ~/.vimrc' | windo so ~/.vimrc or :so $MYVIMRC Or :source ~/.config/nvim/init.vim }}}
"# how to update nvim  {{{
"sudo apt remove neovim -y
"sudo add-apt-repository ppa:neovim-ppa/stable
"<!--NOTE: couldnt get this command to work ^^^-->
"sudo apt-get update
"sudo apt-get install neovim }}}
"# checkhealth https://neovim.io/doc/user/pi_health.html{{{
"run :checkhealth to see if any of the packages you have installed have errors or warnings, or dependencies }}}
"#scroll without moving cursor{{{
"ctrl-e and crtl-y scroll without moving cursor
"ctrl-b ctrl-f page up down
"ctrl-u ctrl-d 1/2 page up down
"105gg go to line 105
"zz move cursor line to center of screen
"zt move cursor line to top of screen }}}
"# added lines to the rc to make it so my cursorline is highlighted only when Im in visual mode{{{
"rn there is an issue, it highlights the cursor in all open verticle splits.
"i tried to fix it with :bufdo set nocul but it dint work
"neither did :bufdo setlocal nocul
"idk for now, will come back later }}}
"# typing terminal commands in vim{{{
":term will open a terminal in vim. 
"To exit insert mode use C-\ C-n. I added hotkeys to make this faster and to accomodate my alt+hjkl movements
"alternatively can either type your command after an exclamation point like so ":!pwd"
"or you can leave your vim session with control+z
"then you can do whatever you want in the command line. 
"after you are done, return to your vim session with 'fd' and then hit enter
"stopped using this because its better to use tmxu for ssh things, but for everything else it might be better }}}
"# neo vim {{{
"https://www.linuxfordevices.com/tutorials/linux/vim-vs-neovim
"basically neo vim is supposed to be a more extensible, more open source version of vim since the original has a gatekeeper maintainer that is keeping the origional project more conservative. 
"neovim also has better support for lsp and lua
"i am mostly interested because its supposed to be able to tap into neovim for vim commands in other applications. So you dont need other extensions or third party apps like vimuim or hunt and peck.... }}}
"# vim sessions{{{
"https://stackoverflow.com/questions/1642611/how-to-save-and-restore-multiple-different-sessions-in-vim
"to make a sesion :mks sessionfilename
"to open a saved session :source -s sessionNameYouCreated
"having lots of trouble finding a central resource for this
"see the man page with :help mksession }}}
"# to switch the current working directory in vimhttps://vim.fandom.com/wiki/Set_working_directory_to_the_current_file{{{
":cd %:p:h
"in these commands, % gives the name of the current file, %:p gives its full path, and %:p:h gives its directory (the "head" of the full path).
"to make this happen automatically use the following in your vimrc
"autocmd BufEnter * silent! lcd %:p:h }}}
"# vim help{{{
"type :vim help to open the help man page
"there are lots of tutorials and help pages
"to open any of the linked pages use :help tutor to open the vim tutor doc for example.
"the help docs normally open in a horizontal split by default.
"you can expand this to full screen with ctrl +w+o
"alternatively, you could open the help window in a new tab: :tab help foo, and then use :q to close it. }}}
"# recording keystrokes https://learnbyexample.gitbooks.io/vim-reference/content/Recording_Macro.html{{{
"this is the first niceish tutorial I found, but it could be better
"use q then a letter to store your recording. ending with q again in normal mode to finish recording
"then use @+letterYouUsed to play it back
"there are a bunch more things you can do, read tutorial
"* good reference for general macro stuff https://vim.fandom.com/wiki/Macros#Viewing_a_macro
"to see all your macros, type : reg
"to see just one type ":reg a" to see the macro for a
""more tips here like how to write a macro out and save it

" really good explanation of how to see and edit all added vim macros https://stackoverflow.com/questions/2689520/clear-all-currently-defined-vim-macros
" comprehensive overview of vim registers https://www.baeldung.com/linux/vim-registers
    
" }}}
"claus said to watch{{{
"https://www.youtube.com/watch?v=434tljD-5C8 and 
"https://youtu.be/n9k9scbTuvQ
"clause github .files repo https://github.com/SenorGato/dotfiles/blob/main/.vimrc }}}
"# disable search when you are done with it{{{
":noh
"you can bind this to a hotkey if you want }}}
"# search command history https://stackoverflow.com/questions/741913/how-do-you-search-through-vims-command-history#:~:text=Press%20Ctrl%2BF%20in%20command,a%20command%20from%20the%20history.{{{
"in normal mode type q: to search history
"or to search /serachhistory types /firstletersof search then use up and down arrows to cycle through suffix matches you have serached for on page }}}
"# find replace {{{
"https://vim.fandom.com/wiki/Search_and_replace
"* :%s/foo/bar/g
"find each occurrence of 'foo' (in all lines), and replace it with 'bar'.
"* :%s/foo/bar/gc
"change each 'foo' to 'bar', but ask for confirmation first.
"* :%s/foo/bar/gci
"change each 'foo' (case insensitive due to the i flag) to 'bar'; ask for confirmation.
"* :%s/foo\c/bar/gc is the same because \c makes the search case insensitive.
"this may be wanted after using :set noignorecase to make searches case sensitive (the default).
"* :%s/foo/bar/gcI
"change each 'foo' (case sensitive due to the I flag) to 'bar'; ask for confirmation.
"* :%s/foo\C/bar/gc is the same because \C makes the search case sensitive.
"this may be wanted after using :set ignorecase to make searches case insensitive.
"to insert a newline or a carriage return use \r "%s/> }}}/. }}} \r/g
" }}}
"# insert text at the beginning of each line{{{
"https://stackoverflow.com/questions/253380/how-to-insert-text-at-beginning-of-a-multi-line-selection-in-vi-vim
"press Esc to enter 'command mode'
"use Ctrl+V to enter visual block mode
"move Up/Downto select the columns of text in the lines you want to comment.
"then hit Shift+i and type the text you want to insert.
"then hit Esc, wait 1 second and the inserted text will appear on every line. }}}
"# fixing errors{{{
"got a bug, 'cannot make changes, "modifiable" is off' 
"according to the internet the solution is to turn modifiable on with :set ma }}}
"# language server notes, having trouble getting it to work{{{
"look into this https://github.com/prabirshrestha/vim-lsp

"# language server protocol (lsp) https://microsoft.github.io/language-server-protocol/overviews/lsp/overview/
"supposedly this is the best way to do language server for nvim, beats other implementations.  }}}
"# extensions to try {{{
"youcomplete me
"vim Surround: https://github.com/tpope/vim-surround
"coc-Pairs: https://github.com/neoclide/coc-pairs
"auto Pairs: https://github.com/jiangmiao/auto-pairs
"vim-Closetag: https://github.com/alvan/vim-closetag
"links to plugins:
"https://github.com/mattn/emmet-vim
"https://github.com/alvan/vim-closetag
"https://github.com/AndrewRadev/tagalo...
""look up syntastic, a code formater

"
"
"
"

" }}}
"# vimwiki alternative to obsidian but in vim, has some functionality that obsidian doesnt, and lacks a few things obsidian has {{{
"you can use vim wiki with github pages to turn your notes into a website which is pretty cool 
"it seems like you can 
"this seems super cool, but the videos i have watched so far have no made it clear you can do graph style linking. 
"i suspect fuzzy finder and a faster grep workflow could do most of the functionality of the graph based system. 
"cause you only need to be able to navigate fast
"from what i can tell you can link shit with a graph style format in vim wiki, so it might work better than obsidian with the md files. }}}
"# introduction to org mode https://www.youtube.com/watch?v=SzA2YODtgK4&t=823s{{{
"seems cool, kinda like vim wiki but maybe more polished??? }}}
"org roam> {{{
"ok this is looks like the best note taking tool i have ever seen almost certainly. 
"https://www.youtube.com/watch?v=HXa5fZjbioA> }}}

"# mkdocs https://github.com/mkdocs/mkdocs{{{
"static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file. It is designed to be easy to use and can be extended with third-party themes, plugins, and Markdown extensions. }}}
"# decent tutorial on how to switch to lua if you want to{{{
"https://vonheikemen.github.io/devlog/tools/configuring-neovim-using-lua/ }}}
"# decent introduction to vimscript language but not much background on the vim environment {{{
"https://learnxinyminutes.com/docs/vimscript/ }}}
"# astrovim, has language server already installed{{{
"https://github.com/AstroNvim/AstroNvim
"gonna try it wish me luck
"ok, installed, packersync not workingjk
"a guy here said to do stuff https://github.com/wbthomason/packer.nvim/issues/834
"gonna take a break on all this
"i moved my init.lua into ~/.config/nvimbackup }}}
"# netrw file explorer https://vonheikemen.github.io/devlog/tools/using-netrw-vim-builtin-file-explorer/{{{
"% to create new file
"lower case d creates new directory
"mt to mark target folder to move stuff to
"mf to mark file to move
"mc to copy files to marked target
"use v on file to open in vertical split, super fucking great
"so netrw has lots of bugs, a little shitty, not good to try to move files in it really, but copying and renaming seems ok
"full tutorial on netrw is pretty good 3rd part https://www.youtube.com/watch?v=9UxMvz6u1K4

"settings for netrw file explorer
let g:netrw_liststyle = 3 " sets default display view you can change with i 
let g:netrw_keepdir = 0 " supposed to make it so moving files works in netrw 

"# how to open another file in vim
"use the :e pathToFileNameFromDirectoryVimWasOpenedFrom
"use :vsp pathToFileNameFromDirectoryVimWasOpenedFrom to open a new file in a vertical split to the left
"to open a split to the right prefix vsp with botright like so 
":botright vsp someFile.txt
"Or set your vim split to be right permanantly with :set splitright
"set splitright "note, to force left prefix vsp with topleft instead of botright
"the path you enter could be just a ., which will open an interactive view of the file system and you can move around in it with j and k, and go up a directory if you go up the the ../ and hit enter.
"i bet there is an extension for this that will let you go back if you hit h.
"* to roate the position of the vim splits use <C-w><C-r>
"* to change the widtth of vim split use <C-w>then plus or minus




" }}}
"jumping around{{{
" https://vim.fandom.com/wiki/Jumping_to_previously_visited_locations
" You can also use g; and g, to move backward and forward in your edit locations.
" ctrl-o and ctrl-i are juspposed to move back by cursor position but
" they dont work for me at all
"# use ctrl ] to jump to topic in vim help files }}}
"# How to view full path of file in Vim{{{
"press 1 followed by Ctrl-G. }}}
"# vim marks https://vim.fandom.com/wiki/Using_marks{{{
"kidna a cool way or returning to a spot aftre you leave it. }}}
"# insert mode movements https://vi.stackexchange.com/questions/10296/navigation-in-insert-mode{{{
"Jesus this doesn't fucking work! Neither method works
"also the ctrl-o doesnt work, fucking annoyed }}}
"# tried to use vim for grading nucamp{{{
"had serious issues with both lite-server -c forgradig.html 
"and live-server forgrading.html
"its fucking frustrating, lite-server throws an error i cant tell why on the doctype line, but not in the file called index.html
"live-server wont load the css for any file but index.html. cant for the life of me tell why, they both like index.html, and no other file names. I could just use index.html for grading, but I would rather not??? nevermidn I did, its slightly more work, but onl cause switching between 2 and 1 with mod sucks
"you can use google-chrome forgrading.html to open a file, but it does not automatically reload. 
"probablem persists in chrome too. 
"it could be an extension, but idk how that would fucking things up }}}
"# this might be the dream note setup https://jonreeve.com/2020/12/my-notetaking-system/{{{
"org mode emacs and a few org mode plugins so you have org mode and then a roam-server to give visualization of notes. }}}
"# autocomands https://elias.rhi.hi.is/vim/autocmd.html{{{
"can be used to execute commands when things happen, I might try to use this for turning on or off autosave. 
"that said, it wont work for nodemon type purposes so ill find something else }}}
"change the number of search results to be greater than 99 https://www.reddit.com/r/neovim/comments/wrj7eu/help_show_the_full_number_of_search_occurrences/{{{
"this looks complex or i would do it now, will have to revisit later 

"
"}}}
" a function to clear all registers in vim, to call use :clearRegisters{{{
function! ClearRegisters()
    let regs='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/-="*+'
    let i=0
    while (i<strlen(regs))
        exec 'let @'.regs[i].'=""'
        let i=i+1
    endwhile
endfunction
 
command! ClearRegisters call ClearRegisters()
" }}}
" fixing vim slowing{{{
" accordin to this, this should speed up the screen update https://stackoverflow.com/questions/37644682/why-is-vim-so-slow
" I have no idea what these do, will have to look up later but they didnt
" seem to fix anything
set timeoutlen=1000
set ttimeoutlen=0

" }}}
"How to see which plugins are making Vim slow?> {{{
"https://stackoverflow.com/questions/12213597/how-to-see-which-plugins-are-making-vim-slow
"Most annoying slow-down of a plain-text editor! [closed]
"https://vi.stackexchange.com/questions/10495/most-annoying-slow-down-of-a-plain-text-editor>  }}}
"
" hotkey to source vimrc
"function! SourceAndInstall()"{{{
"execute "so ~/.config/nvim/init.vim"

"endfunction"}}}
"noremap <C-m> : so ~/.config/nvim/init.vim | PlugInstall

" trying to follow nvim from scratch tutorial{{{
" clause says watch these videos to make vim actually work for you https://www.youtube.com/watch?v=ctH-a-1eUME&list=PLhoH5vyxr6Qq41NFL4GvhFp-WLd5xzIzZ
" https://www.youtube.com/watch?v=5KQK2id3JtI
" first thing to follow i need to clone, and upgrade to .08 so i gotta figure
" that out. 
"
"
"
"
"
"
"
"
"
"
"}}}
"
" open a file and scroll to the bottom {{{
" https://vi.stackexchange.com/questions/6708/open-file-and-scroll-to-bottom-command-line-param
" basically use +$ in the vim command to open the file}}}

"Insert a single character{{{
"https://vim.fandom.com/wiki/Insert_a_single_character#:~:text=Now%2C%20when%20in%20normal%20mode,that%20you%20want%20to%20insert.
":nnoremap <Space> i_<Esc>r
"nnoremap <Leader>i i_<Esc>r
"nnoremap <Leader>,a a_<Esc>r
":nnoremap s :exec "normal i".nr2char(getchar())."\e"<CR>
":nnoremap S :exec "normal a".nr2char(getchar())."\e"<CR>
" note this does work but i dont have time to deal with it rn. will come back
" and make it better later
"}}}
