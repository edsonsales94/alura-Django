# Generated by Django 4.0.2 on 2022-02-14 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0004_receita_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]
