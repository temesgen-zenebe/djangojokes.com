# Generated by Django 4.0.4 on 2022-05-22 19:16

from django.db import migrations, models
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='start_date',
            field=models.DateField(validators=[jobs.models.validate_future_date]),
        ),
    ]