# Generated by Django 2.1.7 on 2019-02-28 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0011_auto_20190228_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='owner',
            field=models.ForeignKey(blank='True', null=True, on_delete=django.db.models.deletion.SET_NULL, to='lists.Profile'),
        ),
    ]
