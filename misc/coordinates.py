import spacepy.coordinates as sc
from spacepy.time import Ticktock

from hapiclient import hapi, hapitime2datetime

server     = 'https://hapi-server.org/servers/SSCWeb/hapi'
dataset    = 'swarma'
parameters = 'X_GSE,Y_GSE,Z_GSE,X_GSM,Y_GSM,Z_GSM'
start      = '2013-11-26T00:00:00Z'
stop       = '2013-11-26T00:01:00Z'

opts       = {'logging': True, 'usecache': True, 'cachedir': './hapicache'}

data, meta = hapi(server, dataset, parameters, start, stop)

xyz_gse = [data['X_GSE'][0],data['Y_GSE'][0],data['Z_GSE'][0]]
xyz_gsm = [data['X_GSM'][0],data['Y_GSM'][0],data['Z_GSM'][0]]

inp = sc.Coords(xyz_gse, 'GSE', 'car')

datetimes = hapitime2datetime(data['Time'])

# Convert from YYYY-DOY to YYYY-MM-DD date format needed by SpacePy
inp.ticks = Ticktock([datetimes[0].strftime('%Y-%m-%dT%H:%M:%S.%f')], 'ISO')

output = inp.convert('GSM', 'car')
xyz_gsm_spacepy = output.data[0]

print('             X_GSM       Y_GSM       Z_GSM ')
print('SSCWeb:  {0:11.8f} {1:11.8f} {2:11.8f}'.format(*xyz_gsm))
print('SpacePy: {0:11.8f} {1:11.8f} {2:11.8f}'.format(*xyz_gsm_spacepy))
