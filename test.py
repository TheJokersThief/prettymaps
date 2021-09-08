#import vsketch
from prettymaps import *
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
import osmnx as ox

ox.utils.config(
    use_cache=True,
    overpass_endpoint="http://192.168.178.45:16340/api",
    # overpass_rate_limit=False
)

# Style parameters
palette = ['#433633', '#FF5E5B']
background_c = '#F2F4CB'
dilate = 100

# Setup figure
fig, ax = plt.subplots(figsize = (10, 10), constrained_layout = True)

# Plot
layers = plot(
    "Ballincollig, Ireland", radius = 500,
    ax = ax,
    layers = {
        'perimeter': {'circle': False, 'dilate': dilate},
        'streets': {
            'width': {
                'primary': 5,
                'secondary': 4,
                'tertiary': 3,
                'residential': 2,
                'footway': 1,
            },
            'circle': False,
            'dilate': dilate
        },
        'building': {
            'tags': {'building': True},
            'union': False,
            'circle': False,
            'dilate': dilate
        },
        'green': {
            'tags': {
                'landuse': ['grass', 'village_green'],
                'leisure': 'park'
            },
            'circle': False,
            'dilate': dilate
        },
    },
    drawing_kwargs = {
        'background': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'hatch': 'ooo...', 'zorder': -1},
        'perimeter': {'fill': False, 'lw': 0, 'zorder': 0},
        'green': {'fc': '#8BB174', 'ec': '#2F3737', 'hatch_c': '#A7C497', 'hatch': 'ooo...', 'lw': 1, 'zorder': 1},
        'water': {'fc': '#a8e1e6', 'ec': '#2F3737', 'hatch_c': '#9bc3d4', 'hatch': 'ooo...', 'lw': 1, 'zorder': 3},
        'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 4},
        'building': {'palette': palette, 'ec': '#2F3737', 'lw': .5, 'zorder': 5},
    }
)

# Set bounds
xmin, ymin, xmax, ymax = layers['perimeter'].bounds
dx, dy = xmax-xmin, ymax-ymin
ax.set_xlim(xmin-.06*dx, xmax+.06*dx)
ax.set_ylim(ymin-.06*dy, ymax+.06*dy)

# Draw left text
ax.text(
    xmin-.06*dx, ymin+.5*dy,
    'Barcelona, Spain',
    color = '#2F3737',
    rotation = 90,
    fontproperties = fm.FontProperties(fname = 'assets/Permanent_Marker/PermanentMarker-Regular.ttf', size = 35),
)
# Draw top text
ax.text(
    xmax-.35*dx, ymax+.02*dy,
    "41° 23′ N, 2° 11′ E",
    color = '#2F3737',
    fontproperties = fm.FontProperties(fname = 'assets/Permanent_Marker/PermanentMarker-Regular.ttf', size = 20),
)

plt.savefig('prints/barcelona.png')
plt.savefig('prints/barcelona.svg')
