# Generated by Django 3.2.5 on 2021-10-25 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestUlgamyApp', '0002_alter_student_test_e_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_test',
            name='e_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student_test',
            name='e_max_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
