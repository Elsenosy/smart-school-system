# Generated by Django 3.0.3 on 2020-05-02 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_material'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='m_type',
            new_name='media_type',
        ),
    ]
