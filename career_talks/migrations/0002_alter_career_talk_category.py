# Generated by Django 3.2.3 on 2021-07-25 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career_talks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career_talk',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='career_talks.Category'),
        ),
    ]