# Generated by Django 3.0.8 on 2020-12-04 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('angebot', '0019_test_angebot_anschlussm'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_angebot',
            name='kundenid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='angebot.Test_Kunde'),
            preserve_default=False,
        ),
    ]
