# Generated by Django 2.0.6 on 2018-07-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180726_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default='abc', max_length=200),
            preserve_default=False,
        ),
    ]