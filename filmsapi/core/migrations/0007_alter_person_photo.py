# Generated by Django 4.1.1 on 2023-05-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_film_description_alter_category_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
