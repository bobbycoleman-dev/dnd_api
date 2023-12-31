# Generated by Django 5.0 on 2023-12-17 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('char_class', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
                ('exp', models.IntegerField()),
                ('str_stat', models.IntegerField(db_column='STR')),
                ('dex_stat', models.IntegerField(db_column='DEX')),
                ('con_stat', models.IntegerField(db_column='CON')),
                ('int_stat', models.IntegerField(db_column='INT')),
                ('wis_stat', models.IntegerField(db_column='WIS')),
                ('cha_stat', models.IntegerField(db_column='CHA')),
                ('background', models.TextField()),
            ],
        ),
    ]
