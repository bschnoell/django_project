# Generated by Django 3.0.8 on 2020-12-04 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('angebot', '0021_auto_20201204_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_angebot',
            name='ojektid',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='angebot.Test_Objekt'),
            preserve_default=False,
        ),
    ]
