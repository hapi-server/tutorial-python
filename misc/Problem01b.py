# ACE Electron, Proton, and Alpha Monitor
# https://cdaweb.gsfc.nasa.gov/registry/hdp/hapi/hapiHtml.html#url=https://cdaweb.gsfc.nasa.gov/hapi&id=AC_K0_EPM
if True:
    dataset    = 'AC_K0_EPM'
    parameters = 'H_lo,Electron_lo,Electron_hi'
    data, meta = hapi(server, dataset, parameters, start, stop, **opts)
    print(data['Time'][0])
    print(data['Time'][-1])
    print(data['H_lo'][0])
    print(data['Electron_lo'][0])
    print(data['Electron_hi'][0])

    hapiplot(data, meta);

