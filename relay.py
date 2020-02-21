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
        resp = requests.get('{}{}'.format(HOST_URL, event['path']),
                                auth=(USERNAME, PASSWORD),
                                params=event['queryStringParameters'])

    if event['httpMethod'] == 'POST':
        resp = requests.post('{}{}'.format(HOST_URL, event['path']),
                                auth=(USERNAME, PASSWORD),
                                data=json.dumps(event['body']),
                                headers={'content-type': 'application/json'})

    logger.info(event)

    response = {
        'statusCode': resp.status_code,
        'body': json.dumps(resp.json()['data'])
    }

    return response
