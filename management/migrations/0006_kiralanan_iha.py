# Generated by Django 5.0.1 on 2024-02-01 17:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_iha_resim'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KIRALANAN_IHA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslangic_tarihi', models.CharField(max_length=100)),
                ('bitis_tarihi', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('iha', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.iha')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]