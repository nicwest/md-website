Vim: filter list by list
========================

I used Vim's built in `filter` function for the first time this week in a pull
request to
[rainbow_parenthesis](https://github.com/kien/rainbow_parentheses.vim/pull/13).
The goal was to filter a list of colour pairs by another list of colours that I
wanted to exclude. Here's a simplified example:

```vim
let colours = ["red", "green", "black", "brown", "blue", "white", "grey"]
let monochrome = ["black", "white", "grey"]
let colours_no_monochrome = filter(colours, "index(monochrome, v:val) < 0")
" ["red", "green", "brown", "blue"]
``` 

`filter` takes two arguments: a list and a string containing a some code. Vim
uses the string as a poor man's anonymous function, and will sequentially pass
all elements in the list through it. The current element of the list is
represented by the `v:val` variable. If this function outputs some that evals to
true the current list element will be added to the returned list, if it evals to
false nothing will be done.

Coming from a python background I fully expected to be able to use something
like `v:val in no_legs` but it seems that `in` in Vim is only a valid operator
in `for` loops. As such we can fall back to `index` which will return the
position of the first matching element in the list. If there is no matching
element the function returns -1. This way `index(no_legs, v:val) < 0` will
return true or false in the same way that you would expect `in` to.
