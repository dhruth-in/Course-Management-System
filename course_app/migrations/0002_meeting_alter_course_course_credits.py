# Generated by Django 5.0.7 on 2024-08-06 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Meeting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("meeting_code", models.CharField(max_length=100)),
                ("meeting_dt", models.DateField(auto_now_add=True)),
                ("meeting_subject", models.CharField(max_length=100)),
                ("meeting_np", models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name="course",
            name="course_credits",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
