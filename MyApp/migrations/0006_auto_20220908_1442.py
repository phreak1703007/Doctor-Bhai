# Generated by Django 2.2.5 on 2022-09-08 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0005_auto_20220906_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='contact',
            field=models.CharField(max_length=11),
        ),
    ]
