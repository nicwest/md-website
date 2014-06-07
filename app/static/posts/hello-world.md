Hello World
===========

I have felt for a while that I would like to write a regular blog. Not because
I have anything particularly interesting to say, but rather to help me be more
decisive (and therefore) quicker when writing other things. That's the idea
anyway! On the plus side I'm actively writing a lot of python so there's
probably something interesting to write about there. I'm currently moving to a 
terminal environment centred around vim so expect vim articles. There may be an
occasional EPUB article, it almost certainly will not be exciting. Finally I'm
currently a junior web developer at [Leto Lab](http://weareleto.com) in london,
and at lunch times I work on becoming 90% burrito. 

###The Blog###

So the blog is basically a simple [flask](http://flask.pocoo.org/) app that
parses [markdown](http://daringfireball.net/projects/markdown/) files using the
[markdown libary](https://pypi.python.org/pypi/Markdown) (which is frickin'
awesome) that I'm hosting on [heroku](http://heroku.com). Source code is
availble [here](https://github.com/nicwest/md-website).

I found out strings containing dates in an [ISO-8601-ish
        format](http://en.wikipedia.org/wiki/ISO_8601) `YYYY-MM-DD HH:mm` are
sortable.  for example:

```python
dates = ["2014-06-07 17:30", "2013-08-17 17:30", "2014-06-07 12:30"]
dates.sort(reverse=True)
print dates
["2014-06-07 17:30", "2014-06-07 12:30", "2013-08-17 17:30"]
```

###Changes to my .vimrc###

How could any action involving typing text into a computer be complete without
adding several lines to [my
        .vimrc](https://github.com/nicwest/.dotfiles/blob/master/vim/.vimrc):

```vim 
autocmd BufNewFile,BufRead *.md set filetype=markdown
autocmd Filetype markdown setlocal tw=80
autocmd Filetype markdown setlocal wm=4
autocmd Filetype markdown setlocal fo=cat 
nnoremap <Leader>fd :set ft=txt<CR>
nnoremap <Leader>fm :set ft=markdown<CR>
```

This is just some basic vim markdown stuff, the first `autocmd` overwrites vim's
default for .md files which is modular2, the next three `autocmd`'s auto wrap my
text lines at 80 chars. However I'm using [higlight.js](http://highlightjs.org/)
and
[fenced_code](http://pythonhosted.org/Markdown/extensions/fenced_code_blocks.html)
to github style code highlighting using ` ```language_name ` code blocks. The
problem is when I want to  write some code in markdown it try's to join lines
under 80 chars and split lines over 80. This is problematic so I have set up a
couple of key bindings to swap to plain text mode and back to markdown. 
