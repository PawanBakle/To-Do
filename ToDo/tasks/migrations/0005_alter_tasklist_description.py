# Generated by Django 4.1.3 on 2024-10-10 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_tasklist_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='description',
            field=models.TextField(default='DESCRIPTION'),
        ),
    ]
