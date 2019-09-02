# my lambda code for canary event

from datetime import datetime

import boto3
import botocore


def count_rows(obj):
    rows = obj.get()['Body'].read().split()
    return len(rows)


def logging(objects, last_added):
    row_count = 0
    file_count = 0
    last_added_rows = 0
    for obj in objects:
        if obj.key == last_added:
            last_added_rows = count_rows(obj)
        else:
            row_count += count_rows(obj)
            file_count += 1
    return row_count / file_count, last_added_rows


get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))


def lambda_handler(event, context):
    print('Running at {}...'.format(event['time']))

    BUCKET_NAME = 'csvcomparision'  # replace with your bucket name
    client = boto3.client('s3')
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET_NAME)

    try:
        objs = client.list_objects_v2(Bucket=BUCKET_NAME)['Contents']
        last_added = [obj['Key'] for obj in sorted(objs, key=get_last_modified)][-1]

        avg, last_added_rows = logging(bucket.objects.all(), last_added)

        msg = "%d rows vs. %d rows" % (avg, last_added_rows)
        print("=======> {}".format(msg))
        return msg
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
    finally:
        print('Check complete at {}'.format(str(datetime.now())))
