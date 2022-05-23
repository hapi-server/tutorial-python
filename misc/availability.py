import sys
import logging

from hapiclient import hapitime2datetime

# Change INFO to WARNING or ERROR to suppress logging messages in this script
logging.basicConfig(level=logging.INFO)

from util import availability

server = 'https://hapi-server.org/servers/SSCWeb/hapi'
datasets = availability(server)

ids = []
starts = []
stops = []
n_max = len(datasets)
#n_max = 50 # Plot only first n_max datasets

# Solution to Working with Metadata I - Basic - 1.

# Create table
n = 0
datasets.reverse()
table = []
for idx, dataset in enumerate(datasets):
    # Pad ids. Assumes max id length is 14 chars.
    id = datasets[idx]["id"]
    idp = '{0:15s}'.format(id)
    line = f'{idp}  {datasets[idx]["startDate"]}  {datasets[idx]["stopDate"]}'
    print(line)
    table.append(line)

    ids.append(id)
    starts.append(hapitime2datetime(datasets[idx]["startDate"])[0])
    stops.append(hapitime2datetime(datasets[idx]["stopDate"])[0])
    n = n + 1
    if n > n_max:
        break

sys.stdout.flush()

from datetime import datetime
logging.info("Writing availability.txt")
with open('availability.txt', 'w', encoding = 'utf-8') as f:
    f.write("Table created on " + datetime.now().isoformat() + "\n\n")
    f.write("\n".join(table))
logging.info("Wrote   availability.txt")

# Solution to Working with Metadata I - Basic - 2.

# Plot
import matplotlib.pyplot as plt
from hapiplot.plot.datetick import datetick

def newfig():
    fig, ax = plt.subplots()
    fig.set_figheight(10)
    fig.set_figwidth(8)
    return ax

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
ax = newfig()
fn = 1
for n in range(len(ids)):
    line, = ax.plot([starts[n], stops[n]], [n, n], linewidth=5)
    lc = line.get_color()
    idx.append(n)
    ax.text(stops[n], n, ' ' + ids[n], color=lc, verticalalignment='center')
    if (n + 1) % 50 == 0:
        figconfig(ax)
        plt.tight_layout()
        fname = f"./availability-{fn}.svg"
        logging.info(f'Writing {fname}')
        plt.savefig(fname, bbox_inches='tight')
        logging.info(f'Wrote   {fname}')
        fn = fn + 1
        ax = newfig()

# Finish last plot, if needed
if (n + 1) % 50 != 0:
    figconfig(ax)
    plt.tight_layout()
    logging.info(f'Writing {fname}')
    plt.savefig(f"./availability-{fn}.svg", bbox_inches='tight')
    logging.info(f'Wrote   {fname}')

