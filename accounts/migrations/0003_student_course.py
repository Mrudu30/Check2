# Generated by Django 4.2.4 on 2023-11-05 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.course'),
        ),
    ]