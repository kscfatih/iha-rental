# Generated by Django 5.0.1 on 2024-02-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_alter_iha_navigasyon_alter_iha_oto_pilot'),
    ]

    operations = [
        migrations.AddField(
            model_name='iha',
            name='resim',
            field=models.ImageField(blank=True, null=True, upload_to='iha_resimleri/'),
        ),
    ]
