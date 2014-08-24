Using Ex mode as a REPL for vimscript
====================================

I'm in the process of writing a vim plugin. I think it might be Stockholm
syndrome, but I'm beginning to like the language. Some of the functions, and
most of the regex, however feel a little inconsistent. Testing these functions 
(and especially the regex) has been a pain in the arse. 

I was about ready to halt writing my project and start writing a buffer based
REPL when I remembered Ex mode(`:h Ex-mode`):

```html
Like Command-line mode, but after entering a command
you remain in Ex mode.  Very limited editing of the
command line.  |Ex-mode|
```

Everyone knows Ex mode right? That annoying mode that no one remembers how
to escape, and serves no obvious purpose? Well I still have no idea what this
mode is actually for. However it makes for an excellent REPL. Well maybe not
REPL maybe just REL as you have to type your own `echo` commands, but it's close
enough.

By this point you have almost certainly rebound the default `Q` keybind for Ex
mode to an infinitely more useful function, however you probably still have 
access to the `gQ` keybind that is (practically) the same.

Quiting Ex mode is the second most important issue and also one of the simplest.
Typing `vi` or `visual` will put you back into to sanity mode.

The RE(P)L
==========

This isn't really a REPL because it won't automatically print after evaluating.
I was thinking about doing some `autocmd` voodoo to automatically prefix my
Ex mode commands with the `echo` command but I don't think it's actually going
to save much time.

Your basic Ex mode RE(P)L experience will probably look something like this:

```vim
Entering Ex mode.  Type "visual" to go to Normal mode.
:let test='TESTING ALL THE THINGS'

:echo test
TESTING ALL THE THINGS
:
```

All hail the glory of the Ex mode RE(P)L! On the face of it this might not look
that exciting however if your doing any thing with regex or functions this is
pretty useful:

```vim
Entering Ex mode.  Type "visual" to go to Normal mode.
:let link='<a href="http://www.vimcasts.org">Vimcasts</a>'

:let pattern='.*\([''"]\)\zs.\+:\/\/.\+\ze\1.*'

:echo link =~ 'FUBAR'
0
:echo link =~ pattern
1
:echo matchstr(link, pattern)
http://www.vimcasts.org
:echo matchstr(link, 'FUBAR')

:
```

Super exciting no? This looks great for single liners right? What about
multi-line code:

```vim
Entering Ex mode.  Type "visual" to go to Normal mode.
:let x=4

:let y=6

:if x < y

:  echo x + y
10
:  endif
:if x > y

:  echo x+y
:  endif
:
```

A bit unusual, but still usable, how about for loops:

```vim
Entering Ex mode.  Type "visual" to go to Normal mode.
:for animal in ['cat', 'dog', 'fish', 'llama']

:  echo animal "goes 'MMMMOOOO!'"
cat goes 'MMMMOOOO!'
:  endfor
dog goes 'MMMMOOOO!'
fish goes 'MMMMOOOO!'
llama goes 'MMMMOOOO!'
:
```

I think this is actually pretty cool, because each line of the for loop is
evaluated separately so you know you are getting the result you expect before you
complete the loop (think of it as a trial run). You might have to prepend some
dummy data to your list if you want to get the output from your original list
without the line by line output however!

Finally functions:

```vim
Entering Ex mode.  Type "visual" to go to Normal mode.
:function! AddNums(x, y)

:  return a:x + a:y
:  endfunction
:echo AddNums(5, 10)
15
:
```

Ex mode also respects your command line settings like wildmenu, so you get some
fairly well scoped tab completion which is lacking in a lot of stock REPL's for
other languages.

I think this is a good use case for Ex mode, and it's very helpful if you are
venturing out of your vimrc for the first time. Happy RE(P)L-ing!
