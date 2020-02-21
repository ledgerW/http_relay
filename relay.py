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
    if event['httpMethod'] == 'GET':
        #response = requests.get(PINNACLE_URL)
        logger.info(event)

    if event['httpMethod'] == 'POST':
        #response = requests.post(PINNACLE_URL, event['body'])
        logger.info(event)

    #print(event)
    #logger.info(event)
    response = {
        "statusCode": 200,
        "body": json.dumps(event)
    }

    return response
