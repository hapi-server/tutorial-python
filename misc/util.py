import os
import pickle
import logging

from hapiclient import hapi

# Change INFO to WARNING or ERROR to suppress logging messages in this script
logging.basicConfig(level=logging.INFO)

# Solution to working with Metadata II.

def availability(server):

    if os.path.exists("availability.pkl"):
        with open('availability.pkl', 'rb') as f:
            logging.info('Reading availability.pkl')
            datasets = pickle.load(f)
            logging.info('Read    availability.pkl')

        return datasets

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

    # Save result so we don't need to recreate when we modify table and plot code.
    with open('availability.pkl', 'wb') as f:
        logging.info('Saving availability.pkl')
        pickle.dump(datasets, f)
        logging.info('Saved  availability.pkl')

    return datasets