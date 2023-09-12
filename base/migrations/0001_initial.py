# Generated by Django 4.2.5 on 2023-09-12 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('stock_minimo', models.IntegerField(blank=True, null=True)),
                ('codigo_de_barras', models.IntegerField(blank=True, null=True)),
                ('precio', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]