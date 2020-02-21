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
    logger.info(event)

    if event['httpMethod'] == 'GET':
        resp = requests.get('{}{}'.format(HOST_URL, event['path']),
                            params=event['queryStringParameters'],
                            headers={'Authorization': event['headers']['Authorization']})

    if event['httpMethod'] == 'POST':
        resp = requests.post('{}{}'.format(HOST_URL, event['path']),
                             data=json.dumps(event['body']),
                             headers={'content-type': 'application/json',
                                      'Authorization': event['headers']['Authorization']})

    logger.info(resp)

    response = {
        'statusCode': resp.status_code,
        'body': json.dumps(resp.json())
    }

    return response
