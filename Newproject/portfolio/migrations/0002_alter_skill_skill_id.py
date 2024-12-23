# Generated by Django 5.1.4 on 2024-12-17 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill_id',
            field=models.CharField(choices=[('1', 'Python'), ('2', 'HTML'), ('3', 'CSS'), ('4', 'Django'), ('5', 'Tailwind'), ('6', 'WordPress')], max_length=1, primary_key=True, serialize=False),
        ),
    ]