# Generated by Django 3.0.8 on 2020-12-14 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angebot', '0034_auto_20201214_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_objekt',
            name='baustoffart',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='test_objekt',
            name='bauweiseart',
            field=models.CharField(default='', max_length=100),
        ),
    ]