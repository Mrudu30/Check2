# Generated by Django 4.2.4 on 2023-11-07 05:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_student_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listening', models.CharField(max_length=3)),
                ('reading', models.CharField(max_length=3)),
                ('writing', models.CharField(max_length=3)),
                ('speaking', models.CharField(max_length=3)),
                ('english', models.FloatField()),
                ('english_out_of', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Textbooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_test_given', models.DateField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.course')),
                ('subject', models.ManyToManyField(to='accounts.subjects')),
                ('textbook', models.ManyToManyField(to='accounts.textbooks')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.exam'),
        ),
    ]