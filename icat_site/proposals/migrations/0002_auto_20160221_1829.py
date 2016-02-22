# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_proposals', '0001_initial'),
        ('symposion_reviews', '0001_initial'),
        ('symposion_schedule', '0002_slot_name'),
        ('proposals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('proposalbase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='symposion_proposals.ProposalBase')),
                ('category', models.IntegerField(choices=[(1, 'Green Economy'), (2, 'Energy'), (3, 'Water & Sanitation'), (4, 'Health'), (5, 'Construction & Infrastructure'), (6, 'Environment & Agriculture'), (7, 'Knowledge & Technology Transfer'), (8, 'Policy, Standards, & Ethics')])),
                ('format', models.IntegerField(choices=[(1, 'Full Paper & Presentation'), (2, 'Poster'), (3, 'Project')])),
                ('recording_release', models.BooleanField(default=True, help_text=b'By submitting your proposal, you agree to give permission to the conference organizers to record, edit, and release audio and/or video of your presentation. If you do not agree to this, please uncheck this box.')),
            ],
            options={
                'verbose_name': 'proposal',
            },
            bases=('symposion_proposals.proposalbase',),
        ),
        migrations.RemoveField(
            model_name='talkproposal',
            name='proposalbase_ptr',
        ),
        migrations.RemoveField(
            model_name='tutorialproposal',
            name='proposalbase_ptr',
        ),
        migrations.DeleteModel(
            name='TalkProposal',
        ),
        migrations.DeleteModel(
            name='TutorialProposal',
        ),
    ]
