# Generated by Django 4.1.3 on 2023-02-24 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_flick_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flick',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]