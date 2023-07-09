# Generated by Django 4.2.2 on 2023-06-21 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('distance', models.PositiveIntegerField()),
                ('markup_factor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('number_in_stock', models.PositiveIntegerField()),
                ('pharmacy', models.ManyToManyField(related_name='medicines', to='app.pharmacy')),
            ],
        ),
    ]
