Leader Key
==========

Some leader key bindings.  

```vim
" map leader to space
let mapleader = "\<Space>"
```

Space is a big, easy to hit key that's in almost exactly the same place on all
key boards. It has little to no use in normal mode and allows access to the full
keyboard without leaving home row. As a secondary I don't like the repurposed
`,` key for the leader, by default this key is the reverse of `;` (repeating the
last `f`, `t`, `F`, or `T`, motion), which is pretty useful for line navigation.

```vim 
" clears search
nnoremap <leader><BS> :noh<cr>

" buffer swap
nnoremap <leader><Tab> <C-^>

" reselect pasted text
nnoremap <leader>v V`]
```

These don't really need much explanation beyond the comments, most of them don't
actually save any key strokes, just move functionality I use a lot into a
clearer place. 


```vim
" put under/over
nnoremap <silent> <leader>pu :pu<CR>
nnoremap <silent> <leader>po :pu!<CR>
```

These are probably two of my most used leader binds. I use them for line
relative put as opposed to the standard cursor relative put. I find that I will
tend to use one of these two bindings by default unless I specifically want
in-line put or know specifically `p` will give me the same output as `:pu` (for
example after `dd` or `yy`). 


```vim
" folding and things
nnoremap <leader><leader> za
nnoremap <leader>r zr
nnoremap <leader>m zm
```

Folds are super cool in terms of vim navigation, these are my most common
actions, `za` toggles the current folder under cursor, `zr` reduces the folding
(adds to `foldlevel`), and `zm` folds more (subtracts from `foldlevel`). I used
to just fold/unfold all, but this gives more control.


```vim
" AG: find things to fix/todo
nnoremap <leader>tf :Ag \(TODO\\|FIXME\)

" quick fix
nnoremap <silent> <leader>qo :copen<CR>
nnoremap <silent> <leader>qq :cclose<CR>
nnoremap <silent> <leader>qc :cex []<CR>
```

Quick fix largely lives as my todo list. In combination with Ag this can be
pretty powerful. I thinking about some exclusions however, as it can get a bit
polluted by third party libraries.
