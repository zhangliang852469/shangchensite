# Generated by Django 2.1.1 on 2018-09-11 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_base', '0003_imformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, upload_to='news_base/static/images', verbose_name='图片'),
        ),
    ]
