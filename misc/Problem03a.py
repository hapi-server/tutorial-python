from hapiclient import hapi

server     = 'https://vires.services/hapi'
dataset    = 'SW_OPER_MAGA_LR_1B'
parameters = 'B_NEC'
start      = '2013-11-25T11:02:52Z'
stop       = '2013-11-25T15:02:52.000Z'
opts       = {'usecache': True, 'logging': False, 'cachedir': './hapicache'}

data, meta = hapi(server, dataset, parameters, start, stop, **opts)

from matplotlib import pyplot as plt
from hapiclient import hapitime2datetime

time_name = meta['parameters'][0]['name']
parameter1_name = meta['parameters'][1]['name']
# Convert data['Time'] elements to Python datetime objects
# Note the difference in tick labels when datetimes are used
plt.figure()
plt.plot(hapitime2datetime(data[time_name]),data[parameter1_name])
plt.gcf().autofmt_xdate()
plt.title('scalar with Time as datetimes');
plt.ylabel(f"{meta['parameters'][1]['name']} in {meta['parameters'][1]['units']}")
plt.legend(["N", "E", "C"])