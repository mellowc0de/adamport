# Generated by Django 4.0.6 on 2022-09-04 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_certificates'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificates',
            name='image',
            field=models.ImageField(default='uploads/certs/ai.png', upload_to=''),
        ),
    ]
