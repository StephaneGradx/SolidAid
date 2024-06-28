# Generated by Django 5.0.4 on 2024-05-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
                ('type', models.CharField(choices=[('benevole', 'Benevole'), ('membre', 'Membre')], max_length=30)),
                ('motif', models.CharField(max_length=1000)),
            ],
        ),
    ]