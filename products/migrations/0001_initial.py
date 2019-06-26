# Generated by Django 2.2 on 2019-06-25 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('kcal', models.IntegerField()),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=3)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=3)),
                ('carbo', models.DecimalField(blank=True, decimal_places=1, max_digits=3)),
                ('fibre', models.DecimalField(blank=True, decimal_places=1, max_digits=3)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]