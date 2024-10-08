# Generated by Django 4.2.14 on 2024-08-01 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('course', models.IntegerField(choices=[(1, 'Starters'), (2, 'Main Course'), (3, 'Desserts')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
