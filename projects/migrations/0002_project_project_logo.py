# Generated by Django 2.0.6 on 2018-06-13 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_logo',
            field=models.FileField(default='Project Image', upload_to=''),
            preserve_default=False,
        ),
    ]