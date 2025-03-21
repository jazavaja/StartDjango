from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
import os
import boto3
from django.core.files.storage import default_storage


class TestFileStorage(TestCase):
    import boto3
    from django.conf import settings

    def test_s3_connection(self):
        s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL
        )

        try:
            response = s3_client.list_objects_v2(Bucket=settings.AWS_STORAGE_BUCKET_NAME)

            if 'Contents' in response:
                print("Connection successful. Files in bucket:")
                for obj in response['Contents']:
                    print(obj['Key'])
            else:
                print("No files in bucket or unable to connect.")

        except Exception as e:
            print(f"Error connecting to S3: {e}")
