import os
import json
import requests
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

HOST_URL = os.environ['HOST_URL']


def main(event, context):
    logger.info(event)

    if event['httpMethod'] == 'GET':
        resp = requests.get('{}{}'.format(HOST_URL, event['path']),
                            params=event['queryStringParameters'],
                            headers={'Authorization': event['headers']['Authorization']})

    if event['httpMethod'] == 'POST':
        resp = requests.post('{}{}'.format(HOST_URL, event['path']),
                             data=event['body'],
                             headers={'content-type': 'application/json',
                                      'Authorization': event['headers']['Authorization']})

    response = {
        'statusCode': resp.status_code,
        'body': json.dumps(resp.json())
    }

    logger.info(response)

    return response
