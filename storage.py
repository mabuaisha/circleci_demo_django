import django.conf
import storages.backends.s3boto3


class StaticStorage(storages.backends.s3boto3.S3Boto3Storage):
    location = 'static'

    def __init__(self, *args, **kwargs):
        kwargs['custom_domain'] = django.conf.settings.AWS_CLOUDFRONT_DOMAIN
        super(StaticStorage, self).__init__(*args, **kwargs)


class MediaStorage(storages.backends.s3boto3.S3Boto3Storage):
    location = 'media'

    def __init__(self, *args, **kwargs):
        kwargs['custom_domain'] = django.conf.settings.AWS_CLOUDFRONT_DOMAIN
        super(MediaStorage, self).__init__(*args, **kwargs)