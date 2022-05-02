import logging

from hapiclient import hapi
from hapiclient import hapitime2datetime

from util import availability

short_run = True # If True, only get data for first three s/c

server = 'https://hapi-server.org/servers/SSCWeb/hapi'
start = "2003-10-31T23:00:00Z"
stop = "2003-10-31T23:59:00Z"

# Create table
start_wanted = hapitime2datetime(start)
stop_wanted  = hapitime2datetime(stop)

datasets = availability(server)

n = 0
for idx, dataset in enumerate(datasets):
    # Pad ids
    id = "{:15s}".format(datasets[idx]["id"])
    start_available = hapitime2datetime(datasets[idx]["startDate"])[0]
    stop_available = hapitime2datetime(datasets[idx]["stopDate"])[0]

    if start_available <= start_wanted and stop_available >= stop_wanted:
        print(f'{id}  {datasets[idx]["startDate"]}  {datasets[idx]["stopDate"]}')
        n = n+1

        logging.info(f'Getting data for {datasets[idx]}')
        data, meta = hapi(server, datasets[idx]["id"], 'Spacecraft_Region', start, stop, logging=False)

        if len(data['Spacecraft_Region']) > 0:
            datasets[idx]["Spacecraft_Region"] = data['Spacecraft_Region'][0]
            datasets[idx]["First_Value"] = data['Time'][0].decode('utf-8')
        else:
            datasets[idx]["Spacecraft_Region"] = None

    if short_run and n > 3:
        break


print(f'\n{n} S/C have ephemeris data from {start} to {stop}')
print(80*"-")
print(f"Spacecraft region for first available value between {start} to {stop}")
print("")
n = 0
for idx, dataset in enumerate(datasets):
    id = "{:15s}".format(datasets[idx]["id"])
    if "Spacecraft_Region" in datasets[idx]:
        n = n + 1
        if datasets[idx]["Spacecraft_Region"] is not None:
            print(f'{id}  {datasets[idx]["Spacecraft_Region"]}\t {datasets[idx]["First_Value"]}')
        else:
            print(f'{id}  No values available')

    if short_run and n > 3:
        break
print(80*"-")
