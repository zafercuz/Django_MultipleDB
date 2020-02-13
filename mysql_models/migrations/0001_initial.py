# Generated by Django 2.2.10 on 2020-02-12 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexImage',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('image_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'index_image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IndexProduct',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'index_product',
                'managed': False,
            },
        ),
    ]
