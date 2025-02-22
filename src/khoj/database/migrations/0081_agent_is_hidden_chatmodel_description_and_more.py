# Generated by Django 5.0.10 on 2025-01-16 23:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0080_speechtotextmodeloptions_ai_model_api"),
    ]

    operations = [
        migrations.AddField(
            model_name="agent",
            name="is_hidden",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="chatmodel",
            name="description",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="chatmodel",
            name="strengths",
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
