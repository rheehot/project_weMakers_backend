# Generated by Django 3.0.1 on 2019-12-30 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brands',
            old_name='main_category_id',
            new_name='main_category',
        ),
        migrations.RenameField(
            model_name='productsubcategories',
            old_name='main_category_id',
            new_name='main_category',
        ),
    ]
