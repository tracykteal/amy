# Generated by Django 2.1 on 2018-09-13 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0153_auto_20180904_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='member_sites',
        ),
        migrations.AddField(
            model_name='membership',
            name='additional_instructor_training_seats',
            field=models.PositiveIntegerField(default=0, help_text='Use this field if you want to grant more seats than the agreement provides for.', verbose_name='Additional instructor training seats'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='seats_instructor_training',
            field=models.PositiveIntegerField(default=0, help_text='Number of seats in instructor trainings', verbose_name='Instructor training seats'),
        ),
    ]
