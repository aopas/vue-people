# Generated by Django 2.0.4 on 2018-04-13 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_auto_20180412_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]