from hapiclient import hapitime2datetime

from util import availability

server = 'https://hapi-server.org/servers/SSCWeb/hapi'
datasets = availability(server)

ids = []
starts = []
stops = []
n_max = len(datasets)
#n_max = 50

# Create table
n = 0
datasets.reverse()
for idx, dataset in enumerate(datasets):
    # Pad ids. Assumes max id length is 14 chars.
    id = datasets[idx]["id"]
    idp = '{0:15s}'.format(id)
    print(f'{idp}  {datasets[idx]["startDate"]}  {datasets[idx]["stopDate"]}')
    ids.append(id)
    starts.append(hapitime2datetime(datasets[idx]["startDate"])[0])
    stops.append(hapitime2datetime(datasets[idx]["stopDate"])[0])
    n = n + 1
    if n > n_max:
        break

# Plot
import matplotlib.pyplot as plt
from hapiplot.plot.datetick import datetick

def newfig():
    fig, ax = plt.subplots()
    fig.set_figheight(10)
    fig.set_figwidth(8)
    return fig, ax

def figconfig(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.grid(axis='x', which='minor', alpha=0.5, linestyle=':')
    ax.grid(axis='x', which='major', color='k', alpha=0.5)
    ax.set_yticks(ticks=[])
    ax.set_title(f'{server}')
    datetick('x')

idx = []
fix, ax = newfig()
for n in range(len(ids)):
    line, = ax.plot([starts[n], stops[n]], [n, n], linewidth=5)
    lc = line.get_color()
    idx.append(n)
    ax.text(stops[n], n, ' ' + ids[n], color=lc, verticalalignment='center')
    if (n + 1) % 50 == 0:
        figconfig(ax)
        fix, ax = newfig()

# Finish last plot, if needed
if (n + 1) % 50 != 0:
    figconfig(ax)
