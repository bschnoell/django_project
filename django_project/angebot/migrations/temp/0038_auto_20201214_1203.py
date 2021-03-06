# Generated by Django 3.0.8 on 2020-12-14 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('angebot', '0037_auto_20201214_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_objekt',
            name='baustoffid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='angebot.Test_Baustoff'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test_objekt',
            name='bauweiseid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='angebot.Test_Bauweise'),
            preserve_default=False,
        ),
    ]
