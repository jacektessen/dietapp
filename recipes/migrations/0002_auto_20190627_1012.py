# Generated by Django 2.2 on 2019-06-27 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190627_1012'),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipes',
            options={'verbose_name_plural': 'Recipes'},
        ),
        migrations.AddField(
            model_name='recipes',
            name='ingredient_2',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='recipes',
            name='product_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_2', to='products.Products'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='ingredient_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='product_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_1', to='products.Products'),
        ),
    ]