# Generated by Django 4.2.2 on 2023-06-14 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_alter_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]