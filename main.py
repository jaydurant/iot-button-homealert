import boto3
import logging
import os
import datetime
from pytz import timezone

# import logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#intialize client
sns = boto3.client('sns')

#os environment variables
name1 = os.environ['name1']
name2 = os.environ['name2']
topic1 = os.environ['topic1']
topic2 = os.environ['topic2']

#cases for each click type
cases = {
    'SINGLE': {
        'name': name1,
        'topic': topic1
    },
    'DOUBLE': {
        'name': name2,
        'topic': topic2
    }
}

timezone = timezone("America/Los_Angeles")


def publish_message(clickType):
    """Message is created by clickType encountered

    Args:
        clickType (string): click type
    Returns
        string: completed message
    """
    message = ''
    if clickType in cases:
        case = cases[clickType]
        today = datetime.datetime.now(timezone).strftime("%a %b %d %Y %I:%M%p")
        message = '{} has arrived home @ {}'.format(case['name'], today)

        logger.info('message {}'.format(message))

        sns.publish(TopicArn=case['topic'], Message=message)

        return message
    else:
        logger.error('no applicable clickType {}'.format(clickType))
        return message


def handler(event,context):
    """Event Handler for AWS Lambda

    Args:
        event (dict): dictionary containing MQTT payload
        context (object): aws lambda context object
    Returns
        string: completed message
    """
    logger.info('event {}'.format(event))

    click_type = event['clickType']

    return publish_message(click_type)