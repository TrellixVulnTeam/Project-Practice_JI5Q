# Generated by Django 2.2.5 on 2019-09-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0005_auto_20190918_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(choices=[('xl', 'XL'), ('s', 'S'), ('l', 'L'), ('fs', 'FS'), ('m', 'M')], max_length=100),
        ),
    ]