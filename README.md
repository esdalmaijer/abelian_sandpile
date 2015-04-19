ABELIAN SANDPILE
----------------

A Python implementation of the super-cool abelian sandpile method. For more info, see these articles on [Wikipedia](http://en.wikipedia.org/wiki/Abelian_sandpile_model), and [Nautilus](http://nautil.us/issue/23/dominoes/the-amazing-autotuning-sandpile).

**abelian_sandpile.py**

The algorithm avalanches all piles at once in each iteration (which works relatively quick).

![simple example](https://github.com/esdalmaijer/abelian_sandpile/abelian_sandpile_10000_100x100.png)

**abelian_sandpile_onebyone.py**

Only one pile is avalanched per iteration (making it super slow).

**multiple_abelian_sandpiles.py**

Not just one pile is avalanched, but 256 are! They're in a fancy pattern, organised using Vogel's method (see: http://blog.marmakoide.org/?p=1).
