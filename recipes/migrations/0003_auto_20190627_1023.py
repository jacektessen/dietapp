# Generated by Django 2.2 on 2019-06-27 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190627_1012'),
        ('recipes', '0002_auto_20190627_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='ingredient_3',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='recipes',
            name='ingredient_4',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='recipes',
            name='ingredient_5',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='recipes',
            name='ingredient_6',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='recipes',
            name='product_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_3', to='products.Products'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='product_4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_4', to='products.Products'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='product_5',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_5', to='products.Products'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='product_6',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_6', to='products.Products'),
        ),
    ]
