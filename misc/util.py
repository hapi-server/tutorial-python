import os
import pickle
import logging

from hapiclient import hapi

# Change INFO to WARNING or ERROR to suppress logging messages in this script
logging.basicConfig(level=logging.INFO)

def availability(server):

    if os.path.exists("availability.pkl"):
        with open('availability.pkl', 'rb') as f:
            datasets = pickle.load(f)
            logging.info('Read availability.pkl')
    else:
        resp = hapi(server)
        logging.info(resp)

        datasets = resp['catalog']
        logging.info(datasets)

        for idx, dataset in enumerate(datasets):
            logging.info(f'Working on dataset id {datasets[idx]}')
            resp = hapi(server, dataset["id"], logging=True)
            startDate = resp["startDate"]
            stopDate = resp["stopDate"]
            # Add start/stop to each element in datasets list
            datasets[idx]["startDate"] = startDate
            datasets[idx]["stopDate"] = stopDate
            logging.info(f'  start = {startDate}\tstop = {stopDate}')

        # Save result so we don't need to recreate when we modify table and plot code.
        with open('availability.pkl', 'wb') as f:
            pickle.dump(datasets, f)
            logging.info('Saved availability.pkl')

    return datasets