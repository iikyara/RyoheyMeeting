# Generated by Django 3.2.3 on 2021-09-20 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210605_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.conference')),
            ],
        ),
    ]
