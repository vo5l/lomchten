# Generated by Django 3.0.6 on 2020-05-14 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200514_2146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['id']},
        ),
    ]