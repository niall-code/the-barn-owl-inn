# Generated by Django 4.2.14 on 2024-08-18 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='contact',
        ),
        migrations.AddField(
            model_name='reservation',
            name='mobile',
            field=models.CharField(default='555 0123', max_length=20),
            preserve_default=False,
        ),
    ]
