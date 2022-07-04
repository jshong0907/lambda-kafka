import sys


def handler(event, context):
    return {
        'statusCode': 200,
        'systemVersion': sys.version,
        'receivedData': event.get('data'),
    }
