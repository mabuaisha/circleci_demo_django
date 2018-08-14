import storages.backends.s3boto3


class StaticStorage(storages.backends.s3boto3.S3Boto3Storage):
    location = 'static'


class MediaStorage(storages.backends.s3boto3.S3Boto3Storage):
    location = 'media'