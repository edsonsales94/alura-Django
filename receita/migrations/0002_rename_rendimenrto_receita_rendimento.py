# Generated by Django 4.0.2 on 2022-02-11 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='rendimenrto',
            new_name='rendimento',
        ),
    ]