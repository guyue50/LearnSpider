# Generated by Django 5.0.7 on 2024-07-31 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0017_topics_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='topics',
            name='published',
            field=models.BooleanField(blank=True, default=False, help_text='是否发布', null=True),
        ),
    ]
