# Generated by Django 5.0.3 on 2024-10-23 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_numero_quarto_quarto_numero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quarto',
            name='max_pessoas_quarto',
        ),
        migrations.AddField(
            model_name='quarto',
            name='capacidade',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quarto',
            name='numero',
            field=models.IntegerField(),
        ),
    ]