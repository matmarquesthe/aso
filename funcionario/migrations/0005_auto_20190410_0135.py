# Generated by Django 2.2 on 2019-04-10 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0004_auto_20190410_0126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='date_aso',
            new_name='data_de_Admissao',
        ),
    ]
