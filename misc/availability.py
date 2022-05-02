from util import availability

server = 'https://hapi-server.org/servers/SSCWeb/hapi'
datasets = availability()

# Create table
for idx, dataset in enumerate(datasets):
    # Pad ids. Assumes max id length is 14 chars.
    id = "{:15s}".format(datasets[idx]["id"])
    print(f'{id}  {datasets[idx]["startDate"]}  {datasets[idx]["stopDate"]}')

