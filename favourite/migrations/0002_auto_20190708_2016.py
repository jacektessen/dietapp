# Generated by Django 2.2 on 2019-07-08 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favouriterecipe',
            old_name='recipe_id',
            new_name='recipe',
        ),
    ]
