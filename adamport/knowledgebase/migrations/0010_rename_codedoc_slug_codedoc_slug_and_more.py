# Generated by Django 4.0.6 on 2022-08-06 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgebase', '0009_rename_slug_codedoc_codedoc_slug_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='codedoc',
            old_name='codedoc_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='doctype',
            old_name='doctype_slug',
            new_name='slug',
        ),
    ]
