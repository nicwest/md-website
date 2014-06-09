Highlight.js Pull Request
=========================

I don't really contribute to open source projects, however I use them all day
every day. This makes me feel bad. As such new target will be submitting one
pull request to an open source project every week.

###Highlight.js###

My first pull request is adding [w0ng's hybrid](http://github.com/w0ng/hybrid)
vim theme to the code highlighting script
[highlight.js](http://highlightjs.org/).

Highlight.js is pretty awesome, it's got syntax files for pretty much every
language under the sun, and most popular themes. Sadly it didn't have hybrid, a
mix of [ Tomorrow nights ](https://github.com/chriskempson/tomorrow-theme)
colour pallet and [ Jelly beans ](https://github.com/nanotech/jellybeans.vim)
syntax groups (it does however have both Tomorrow night and ir_black which jelly
beans is based on).

Porting in the end was relatively painless as vim's code groups seem to align
almost perfectly with highlight's (coincidence? I think not). There are a few
discrepancies, and I would advice anyone going down a similar route to avoid
language based classes to produce an exact replica. I did this first for the 22
base languages (plus django and viml), and decided although I was matching vim
pretty much perfectly, the results were inconsistent on a language to language
basis (it also took a long time).

Here's a sample, it's not perfect but it's pretty damn close:

```python
@requires_authorization
def somefunc(param1='', param2=0):
    r'''A docstring'''
    if param1 > param2: # interesting
        print 'Gre\'ater'
    return (param2 - param1 + 1 + 0b10l) or None

class SomeClass:
    pass

>>> message = '''interpreter
... prompt'''
```

![hybrid sample](/static/images/hybridsample.png)
