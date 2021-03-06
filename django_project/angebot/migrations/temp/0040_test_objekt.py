# Generated by Django 3.0.8 on 2020-12-14 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('angebot', '0039_auto_20201214_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_Objekt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeichnung', models.CharField(blank=True, default='', max_length=100)),
                ('dickeaussenwand', models.IntegerField(blank=True, default='0', null=True)),
                ('dickedaemmung', models.IntegerField(default='0')),
                ('uwert', models.IntegerField(default='0')),
                ('fensterqualitaet', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('angebotid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='angebot.Test_Angebot')),
                ('baustoffid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='angebot.Test_Baustoff')),
                ('bauweiseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='angebot.Test_Bauweise')),
            ],
        ),
    ]
