# Generated by Django 4.1.5 on 2023-02-11 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Noms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="food_model",
            name="food_eater",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="food_model",
            name="food_potassium",
            field=models.IntegerField(
                default=0, help_text="mg", verbose_name="Potassium"
            ),
        ),
        migrations.AlterField(
            model_name="food_model",
            name="food_calories",
            field=models.IntegerField(
                default=0, help_text="cal", verbose_name="Calories"
            ),
        ),
        migrations.AlterField(
            model_name="food_model",
            name="food_carb",
            field=models.IntegerField(
                default=0, help_text="g", verbose_name="Total Carbohydrate"
            ),
        ),
        migrations.AlterField(
            model_name="food_model",
            name="food_date",
            field=models.DateField(verbose_name="Date of meal:"),
        ),
        migrations.AlterField(
            model_name="food_model",
            name="food_fat",
            field=models.IntegerField(
                default=0, help_text="g", verbose_name="Total Fat"
            ),
        ),
        migrations.AlterField(
            model_name="food_model",
            name="food_fiber",
            field=models.IntegerField(
                default=0, help_text="g", verbose_name="Dietary Fiber"
            ),
        ),
        migrations.AlterField(
            model_name="food_model",
            name="food_name",
            field=models.CharField(max_length=100, verbose_name="Meal Name"),
        ),
        migrations.AlterField(
            model_name="food_model",
            name="food_protein",
            field=models.IntegerField(default=0, help_text="g", verbose_name="Protein"),
        ),
        migrations.AlterField(
            model_name="food_model",
            name="food_saturatedfat",
            field=models.IntegerField(
                default=0, help_text="g", verbose_name="Saturated Fat"
            ),
        ),
        migrations.AlterField(
            model_name="food_model",
            name="food_sodium",
            field=models.IntegerField(default=0, help_text="mg", verbose_name="Sodium"),
        ),
        migrations.AlterField(
            model_name="food_model",
            name="food_time",
            field=models.TimeField(verbose_name="Time of meal:"),
        ),
    ]