# Generated by Django 3.0.1 on 2020-03-13 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_productoptiondetails_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='EventProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Event')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Products')),
            ],
            options={
                'db_table': 'event_products',
            },
        ),
    ]