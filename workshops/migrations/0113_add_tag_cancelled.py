# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-30 06:37
from __future__ import unicode_literals

from django.db import migrations, models


def add_tag_cancelled(apps, schema_editor):
    Tag = apps.get_model('workshops', 'Tag')
    Tag.objects.get_or_create(name='cancelled',
                              details='Events that were supposed to happen but'
                                      ' due to some circumstances got '
                                      'cancelled')


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0112_sponsorship_contact'),
    ]

    operations = [
        migrations.RunPython(add_tag_cancelled),
        migrations.AlterField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(help_text="<ul><li><i>stalled</i> — for events with lost contact with the host or TTT events that aren't running.</li><li><i>unresponsive</i> – for events whose hosts and/or organizers aren't going to send us attendance data.</li><li><i>cancelled</i> — for events that were supposed to happen, but due to some circumstances got cancelled.</li></ul>", to='workshops.Tag'),
        ),
    ]
