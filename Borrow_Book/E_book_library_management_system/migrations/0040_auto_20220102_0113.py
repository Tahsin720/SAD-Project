# Generated by Django 3.2.9 on 2022-01-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_book_library_management_system', '0039_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
