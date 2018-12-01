# Generated by Django 2.1.3 on 2018-12-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='u',
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='desc',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
