# Generated by Django 4.1.6 on 2023-02-09 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_alter_game_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="correct",
            field=models.IntegerField(
                choices=[(1, "#1"), (2, "#2"), (3, "#3"), (4, "#4")], default=1
            ),
            preserve_default=False,
        ),
    ]