# Generated by Django 3.2 on 2024-07-02 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping_name', models.CharField(max_length=100)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzas.Pizza')),
            ],
        ),
    ]