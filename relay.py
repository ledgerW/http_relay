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
    print(USERNAME)
    if event['httpMethod'] == 'GET':
        response = requests.get('{}{}'.format(HOST_URL, event['path']),
                                auth=(USERNAME, PASSWORD),
                                params=event['queryStringParameters'])

    if event['httpMethod'] == 'POST':
        response = requests.post('{}{}'.format(HOST_URL, event['path']),
                                auth=(USERNAME, PASSWORD),
                                data=json.dumps(event['body']),
                                headers={'content-type': 'application/json'})

    logger.info(event)

    return response
