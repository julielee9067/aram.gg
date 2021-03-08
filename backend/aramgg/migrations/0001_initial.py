# Generated by Django 3.1.7 on 2021-03-08 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=40, unique=True)),
                ("level", models.IntegerField()),
                ("profile_icon", models.IntegerField()),
                ("last_updated", models.BigIntegerField(blank=True, null=True)),
                ("account_id", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Champion",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("champion_id", models.IntegerField()),
                ("win", models.IntegerField(default=0)),
                ("loss", models.IntegerField(default=0)),
                ("kill", models.IntegerField(default=0)),
                ("death", models.IntegerField(default=0)),
                ("assist", models.IntegerField(default=0)),
                ("total_damage_done", models.IntegerField(default=0)),
                ("total_damage_taken", models.IntegerField(default=0)),
                ("total_healing_done", models.IntegerField(default=0)),
                ("total_game_length", models.IntegerField(default=0)),
                ("total_gold_spent", models.IntegerField(default=0)),
                ("total_gold_earned", models.IntegerField(default=0)),
                ("largest_killing_spree", models.IntegerField(default=0)),
                ("num_double_kill", models.IntegerField(default=0)),
                ("num_triple_kill", models.IntegerField(default=0)),
                ("num_quadra_kill", models.IntegerField(default=0)),
                ("num_penta_kill", models.IntegerField(default=0)),
                ("num_legendary_kill", models.IntegerField(default=0)),
                ("num_max_kill", models.IntegerField(default=0)),
                ("num_max_death", models.IntegerField(default=0)),
                ("num_max_assist", models.IntegerField(default=0)),
                ("most_gold_spent", models.IntegerField(default=0)),
                ("most_gold_earned", models.IntegerField(default=0)),
                ("most_damage_done", models.IntegerField(default=0)),
                ("most_damage_taken", models.IntegerField(default=0)),
                ("most_healing_done", models.IntegerField(default=0)),
                ("longest_game_length", models.IntegerField(default=0)),
                ("num_max_double_kill", models.IntegerField(default=0)),
                ("num_max_triple_kill", models.IntegerField(default=0)),
                ("num_max_quadra_kill", models.IntegerField(default=0)),
                ("num_max_penta_kill", models.IntegerField(default=0)),
                ("num_max_legendary_kill", models.IntegerField(default=0)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="aramgg.user",
                    ),
                ),
            ],
        ),
    ]
