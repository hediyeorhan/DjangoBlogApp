# Generated by Django 2.0.3 on 2020-03-29 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20200329_1538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
    ]