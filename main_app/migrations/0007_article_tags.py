# Generated by Django 5.0.4 on 2024-04-30 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_tag_remove_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='main_app.tag'),
        ),
    ]
