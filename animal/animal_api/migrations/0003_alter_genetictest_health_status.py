# Generated by Django 5.1.4 on 2024-12-10 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_api', '0002_alter_genetictest_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genetictest',
            name='health_status',
            field=models.CharField(max_length=150, verbose_name='Состояние здоровья'),
        ),
    ]
