import os
import json
import requests
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

HOST_URL = os.environ['HOST_URL']
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']


def main(event, context):
    if event['body']['method'] == 'GET':
        logger.info(event)
        response = requests.get('{}{}'.format(HOST_URL, event['body']['path']),
                                auth=(USERNAME, PASSWORD),
                                params=event['body']['params'])

    if event['body']['method'] == 'POST':
        logger.info(event)
        response = requests.post('{}{}'.format(HOST_URL, event['body']['path']),
                                auth=(USERNAME, PASSWORD),
                                data=event['body']['body'],
                                headers = {'content-type': 'application/json'})

    #print(event)
    #logger.info(event)
    #response = {
    #    "statusCode": 200,
    #    "body": json.dumps(event)
    #}

    return response
