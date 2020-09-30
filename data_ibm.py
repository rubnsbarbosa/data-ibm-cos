#!/usr/local/bin/python
import pandas as pd
import ibm_botocore.client
import ibm_boto3
from io import StringIO
import logging
import os
import sys

from config import cos_client, cos_resource

logging.basicConfig(stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)


def upload_to_bucket(cos, bucket_name, filename):
    logger.info('Uploading {} to IBM bucket {}...'.format(filename, bucket_name))
    try:
        cos.upload_file(Filename=filename, Bucket=bucket_name, Key=os.path.basename(filename))
        logger.info('Upload completed')
    except Exception as e:
        logger.error("Upload failed!")
        logger.exception(e)


def merge_files(cos, bucket_name, prefix):
    logger.info('Merging files...')
    try:
        bucket = cos.Bucket(bucket_name)
        prefix_objects = bucket.objects.filter(Prefix=prefix)

        prefix_df = []
        for _object in prefix_objects:
            body = _object.get()['Body'].read().decode('utf-8')
            df = pd.read_csv(StringIO(body), header=None, dtype='object')
            prefix_df.append(df)
        return pd.concat(prefix_df)
        logger.info('Merge completed')
    except Exception as e:
        logger.error("Upload failed!")
        logger.exception(e)


def put_file_bucket(cos, file_body, bucket_name, file_name):
    logger.info('Puting file on bucket...')
    try:
        cos.put_object(Body=file_body, Bucket=bucket_name, Key="{}.csv".format(file_name))
        logger.info('Put file on bucket completed')
    except Exception as e:
        logger.error("Upload failed!")
        logger.exception(e)


if __name__ == "__main__":
    print(ibm_boto3.__version__)

    upload_to_bucket(cos_client, 'event-bucket', '20200702-14-c838b4d11fa5.csv')
    upload_to_bucket(cos_client, 'event-bucket', '20200702-14-c838b4d11fa6.csv')

    res = merge_files(cos_resource, 'event-bucket', '20200702-14')
    file_merged = res.to_csv(index=False, header=False)
    print(file_merged)

    put_file_bucket(cos_client, file_merged, 'event-bucket', '20200702/14/merged-final')
