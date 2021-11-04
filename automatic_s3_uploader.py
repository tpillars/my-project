from secrets import access_key, secret_access_key

import boto3
import os

# can access all s3 resources that this access key has permission to (which is full access)
# can upload files and download files using this  client
client = boto3.client('s3',
                      aws_access_key_id = access_key,
                      aws_secret_access_key = secret_access_key)

for file in os.listdir(): # taking every file in your working dir
    if '.py' in file: # files ending in .py = python files
        upload_file_bucket = 'youtube-tutorial-bucket' # designate bucket to upload into
        upload_file_key = 'python/' + str(file)  # pass file to directory "python" keeping original name
        client.upload_file(file, upload_file_bucket, upload_file_key) # actual command to do the uplaod

'''
$ python3 automatic_s3_uploader.py
'''