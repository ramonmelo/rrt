
from matplotlib import pyplot
from shapely.geometry import box
from descartes import PolygonPatch

BLUE = '#6699cc'
GRAY = '#999999'

def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color=GRAY, linewidth=3, solid_capstyle='round', zorder=1)

fig = pyplot.figure(1, figsize=(50, 50), dpi=180)

ax = fig.add_subplot(111)

boundary = box(0, 0, 200, 200)

patch1 = PolygonPatch(boundary, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
ax.add_patch(patch1)

pyplot.show()
