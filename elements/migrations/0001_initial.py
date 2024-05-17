# Generated by Django 5.0.6 on 2024-05-13 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('definition', models.TextField()),
                ('example', models.URLField(blank=True, default=' ', null=True)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
