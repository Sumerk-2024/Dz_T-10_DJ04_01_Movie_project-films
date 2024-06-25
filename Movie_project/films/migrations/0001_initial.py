# Generated by Django 5.0.6 on 2024-06-25 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название фильма')),
                ('description', models.TextField(verbose_name='Описание фильма')),
                ('review', models.TextField(verbose_name='Отзыв')),
            ],
        ),
    ]
