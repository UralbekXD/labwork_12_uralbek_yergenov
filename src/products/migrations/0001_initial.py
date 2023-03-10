# Generated by Django 4.1.6 on 2023-02-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование товара')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание товара')),
                ('image', models.URLField(blank=True, max_length=1024, null=True, verbose_name='Фото товара')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Остаток')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('category', models.CharField(choices=[('electronics', 'электроника'), ('fruits', 'фрукты'), ('cosmetics', 'косметика'), ('drinks', 'напитки'), ('meat', 'мясо'), ('other', 'разное')], default='other', max_length=256)),
            ],
        ),
    ]
