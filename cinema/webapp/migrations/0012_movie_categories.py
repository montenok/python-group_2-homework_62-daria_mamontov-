# Generated by Django 2.1.7 on 2019-03-13 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='film_category', to='webapp.Category', verbose_name='Categories'),
        ),
    ]