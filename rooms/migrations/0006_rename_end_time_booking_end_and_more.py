# Generated by Django 4.2.2 on 2023-06-10 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_remove_booking_name_booking_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='end_time',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='start_time',
            new_name='start',
        ),
    ]