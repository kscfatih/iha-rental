# Generated by Django 5.0.1 on 2024-02-01 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_alter_kiralanan_iha_baslangic_tarihi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kiralanan_iha',
            name='baslangic_tarihi',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='kiralanan_iha',
            name='bitis_tarihi',
            field=models.DateTimeField(),
        ),
    ]
