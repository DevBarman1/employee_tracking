# Generated by Django 5.0.1 on 2024-04-07 17:07

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_App', '0004_featuredin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreeEasySteps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor_uploader.fields.RichTextUploadingField()),
                ('desc', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]
