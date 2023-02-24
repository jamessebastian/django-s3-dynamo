from django.db import models
import os
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute

class Flick2(Model):
    class Meta:
        table_name = os.getenv('DYNAMO_TABLE_NAME2'),
        region = 'us-east-2',
        aws_access_key_id = os.getenv('AWS_S3_ACCESS_KEY_ID2'),
        aws_secret_access_key = os.getenv('AWS_S3_SECRET_ACCESS_KEY2'),

    id = NumberAttribute(hash_key=True)
    title = UnicodeAttribute()
    description = UnicodeAttribute()
    tags = UnicodeAttribute()
    picture = UnicodeAttribute()

class Flick(models.Model):
    # id = models.CharField(primary_key=True, max_length=100)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    tags = models.CharField(max_length=300)
    picture = models.FileField(upload_to='media/')

    