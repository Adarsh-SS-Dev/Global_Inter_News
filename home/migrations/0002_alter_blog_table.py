# Generated by Django 4.1.7 on 2023-05-16 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='blog',
            table='home_blog',
        ),
    ]
