# Generated by Django 4.2.2 on 2023-06-10 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_alter_booking_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='name',
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rooms.room'),
            preserve_default=False,
        ),
    ]
