# Generated by Django 3.2.3 on 2021-07-24 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_centers', '0013_auto_20210724_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='research_center',
            name='video',
            field=models.CharField(max_length=500, null=True, verbose_name='Embeded Url'),
        ),
    ]