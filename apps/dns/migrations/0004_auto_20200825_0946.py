# Generated by Django 3.0.6 on 2020-08-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dns', '0003_dynamicentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamicentry',
            name='value',
            field=models.TextField(blank=True, null=True),
        ),
    ]
