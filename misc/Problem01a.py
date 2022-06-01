from hapiclient import hapi, hapitime2datetime

server     = 'https://cdaweb.gsfc.nasa.gov/hapi'
dataset    = 'AC_H0_MFI'
parameters = 'SC_pos_GSE'
start      = '1997-09-03T00:00:00Z'
stop       = '1997-09-03T00:59:00.000Z'

data_cdaweb, meta_cdaweb = hapi(server, dataset, parameters, start, stop)

xyz_gse_cdaweb = list(data_cdaweb[0][1]/6371.)

server     = 'http://hapi-server.org/servers/SSCWeb/hapi'
dataset    = 'ace'
parameters = 'X_GSE,Y_GSE,Z_GSE'

data_sscweb, meta_sscweb = hapi(server, dataset, parameters, start, stop)

xyz_gse_sscweb = [data_sscweb['X_GSE'][1],data_sscweb['Y_GSE'][1],data_sscweb['Z_GSE'][1]]

time_cdaweb = data_cdaweb['Time'][0].decode()

# Convert from YYYY-DOY to YYYY-MM-DD date format
time_sscweb = hapitime2datetime([data_sscweb['Time'][0]])[0].strftime('%Y-%m-%dT%H:%M:%S.%fZ')

# Time stamps are not idential. For a better comparison, use interpolation
# or find time values that exactly match between SSCWeb and CDAWeb data.
print('        {0:13s}{1:13s}{2:13s}'.format('X_GSE [R_E]', 'Y_GSE [R_E]', 'Z_GSE [R_E]'))
print('SSCWeb: {0:<13.8f}{1:<13.8f}{2:<13.8f}\t on {3:s}'.format(*xyz_gse_cdaweb, time_sscweb))
print('CDAWeb: {0:<13.8f}{1:<13.8f}{2:<13.8f}\t on {3:s}'.format(*xyz_gse_sscweb, time_cdaweb))