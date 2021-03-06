# Generated by Django 2.1.2 on 2018-10-27 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0158_curriculum_workshoprequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshoprequest',
            name='admin_comment',
            field=models.TextField(blank=True, verbose_name='Admin comment'),
        ),
        migrations.AddField(
            model_name='workshoprequest',
            name='event',
            field=models.OneToOneField(blank=True, help_text='Link to the event instance created or otherwise related to this object.', null=True, on_delete=django.db.models.deletion.PROTECT, to='workshops.Event', verbose_name='Linked event object'),
        ),
        migrations.AlterField(
            model_name='workshoprequest',
            name='self_organized_github',
            field=models.URLField(blank=True, help_text='Please provide URL.', max_length=255, verbose_name='Link to workshop GitHub page'),
        ),
    ]
