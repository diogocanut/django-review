# Generated by Django 2.1.5 on 2019-01-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default='1', max_length=2),
        ),
    ]
