# Generated by Django 4.1.3 on 2023-02-24 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_flick_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flick',
            name='uploaded_at',
        ),
    ]