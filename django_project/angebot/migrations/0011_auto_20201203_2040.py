# Generated by Django 3.0.8 on 2020-12-03 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angebot', '0010_auto_20201203_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_angebot',
            name='anschlussL',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='test_angebot',
            name='anschlussM',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='test_angebot',
            name='anschlussS',
            field=models.IntegerField(default='0'),
        ),
    ]
