# Implementation of the Abelian Sandpile Model, originally created by Per Bak,
# Chao Tang, and Kurt Wiesenfeld (1987). For more information, follow this url:
# http://nautil.us/issue/23/dominoes/the-amazing-autotuning-sandpile

# NOTE: this is a quick implementation, that re-divides all piles that are too
# high in each iteration simultaneously. For people that like efficiency, like
# the Germans.

import time
import numpy
from matplotlib import pyplot

# size of the pile-space (each pixel is a pile)
SIZE = (200, 200)

# size of the starting-point space
PSIZE = (100,100)

# maximum number of stackable sand grains that will cause a tople
# (should be dividable by 4!)
MAXH = 4

# first pile
FPH = 10000

# starting points, in a nice patern (Vogel's method)
# (copied from: http://blog.marmakoide.org/?p=1)
n = 256
radius = numpy.sqrt(numpy.arange(n) / float(n))
golden_angle = numpy.pi * (3 - numpy.sqrt(5))
theta = golden_angle * numpy.arange(n)
points = numpy.zeros((n, 2))
points[:,0] = numpy.cos(theta)
points[:,1] = numpy.sin(theta)
points *= radius.reshape((n, 1))

# reshape to fit current figure
points = (points + 1.0) / 2.0
points[:,0] = points[:,0] * PSIZE[0]
points[:,1] = points[:,1] * PSIZE[1]
points = points.astype(int)

# sand field
field = numpy.zeros((SIZE[0]+2,SIZE[1]+2))
field[points[:,0]+1,points[:,0]+1] += FPH

# starting time and iteration
i = 0
t0 = time.time()

# run until a stable state is reached
while numpy.max(field) >= MAXH:

	# find the highest pile
	toohigh = field >= MAXH
	
	# decrease piles
	field[toohigh] -= MAXH
	
	# increase piles
	field[1:,:][toohigh[:-1,:]] += MAXH / 4
	field[:-1,:][toohigh[1:,:]] += MAXH / 4
	field[:,1:][toohigh[:,:-1]] += MAXH / 4
	field[:,:-1][toohigh[:,1:]] += MAXH / 4

	# reset the overspill
	field[0:1,:] = 0
	field[1+SIZE[0]:,:] = 0
	field[:,0:1] = 0
	field[:,1+SIZE[1]:] = 0
	
	# increase number of iterations
	i += 1

# ending time
t1 = time.time()
print("%d iterations in %.2f seconds" % (i, t1-t0))

# show piles
field = field[1:1+SIZE[0],1:1+SIZE[1]]
fig = pyplot.figure(figsize=(10.0,10.0), dpi=100.0, frameon=False)
ax = pyplot.Axes(fig, [0,0,1,1])
ax.set_axis_off()
fig.add_axes(ax)
ax.imshow(field / numpy.max(field), cmap='gray', vmin=0, vmax=1)
#ax.plot(points[:,0], points[:,1], 'o', color='red')
pyplot.savefig("abelian_sandpiles_%d_%dx%d.png" % (FPH,SIZE[0],SIZE[1]))
pyplot.show()

