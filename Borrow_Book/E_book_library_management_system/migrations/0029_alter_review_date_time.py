# Generated by Django 3.2.9 on 2021-12-24 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_book_library_management_system', '0028_review_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 24, 21, 33, 39, 567614)),
        ),
    ]
