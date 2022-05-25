from hapiclient import hapi, hapitime2datetime

server     = 'https://cdaweb.gsfc.nasa.gov/hapi'
dataset    = 'AC_H0_SWE'
parameters = 'Np'
start      = '1998-09-03T00:00:00Z'
stop       = '1998-09-03T00:59:00.000Z'

data1, meta1 = hapi(server, dataset, parameters, start, stop)

server     = 'https://cdaweb.gsfc.nasa.gov/hapi'
dataset    = 'AC_H2_SWE'
parameters = 'Np'
start      = '1998-09-03T00:00:00Z'
stop       = '1998-09-03T00:59:00.000Z'

data2, meta2 = hapi(server, dataset, parameters, start, stop)
