# Generated by Django 4.2.5 on 2023-10-30 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('userEmail', models.EmailField(max_length=45)),
                ('userNickname', models.CharField(max_length=8)),
                ('userAge', models.IntegerField()),
                ('userSex', models.IntegerField()),
                ('userWeight', models.IntegerField()),
                ('userWD', models.CharField(max_length=10)),
                ('anaerobicScore', models.FloatField(default=0.0)),
                ('aerobicScore', models.FloatField(default=0.0)),
                ('Score', models.FloatField(default=0.0)),
                ('AgeRank', models.IntegerField(blank=True, null=True)),
                ('CustomRank', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'userTBL',
                'managed': False,
            },
        ),
    ]
