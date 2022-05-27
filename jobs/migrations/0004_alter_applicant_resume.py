# Generated by Django 4.0.4 on 2022-05-27 05:10

from django.db import migrations, models
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_applicant_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='resume',
            field=models.FileField(blank=True, help_text='PDFs only', upload_to='private/resumes', validators=[jobs.models.validate_pdf]),
        ),
    ]