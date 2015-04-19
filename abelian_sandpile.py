# Implementation of the Abelian Sandpile Model, originally created by Per Bak,
# Chao Tang, and Kurt Wiesenfeld (1987). For more information, follow this url:
# http://nautil.us/issue/23/dominoes/the-amazing-autotuning-sandpile

import numpy
from matplotlib import pyplot

# size of the pile-space (each pixel is a pile)
SIZE = (100, 100)

# maximum number of stackable sand grains that will cause a tople
MAXH = 4

# first pile
FPH = 100
MPC = (49,49)

# sand field
field = numpy.zeros((SIZE[0]+20,SIZE[1]+20))
field[MPC[0]+10,MPC[1]+10] += FPH

# run until a stable state is reached
while numpy.max(field) >= MAXH:

	# find the highest pile
	highest = numpy.argmax(field.reshape(1,field.size))
	x = int(highest) / int(field.shape[0])
	y = highest % field.shape[0]
	
	# divide pile
	field[x,y] -= MAXH
	field[x-1,y] += MAXH / 4
	field[x+1,y] += MAXH / 4
	field[x,y-1] += MAXH / 4
	field[x,y+1] += MAXH / 4

	# reset the overspill
	field[0:10,:] = 0
	field[10+SIZE[0]:,:] = 0
	field[:,0:10] = 0
	field[:,10+SIZE[1]:] = 0

# show piles
field = field[10:10+SIZE[0],10:10+SIZE[1]]
fig = pyplot.figure(figsize=(10.0,10.0), dpi=100.0, frameon=False)
ax = pyplot.Axes(fig, [0,0,1,1])
ax.set_axis_off()
fig.add_axes(ax)
ax.imshow(field / numpy.max(field), cmap='hot', vmin=0, vmax=1)
pyplot.savefig("abelian_sandpile.png", frameon=False)
pyplot.show()

