from django.db import models
from django.utils.translation import ugettext as _

from symposion.proposals.models import ProposalBase


class Proposal(ProposalBase):

    # Proposal Category
    # ~~~~~~~~~~~~~~~~~

    CATEGORY_GREEN_ECONOMY = 1
    CATEGORY_ENERGY = 2
    CATEGORY_WATER___SANITATION = 3
    CATEGORY_HEALTH = 4
    CATEGORY_CONSTRUCTION___INFRASTRUCTURE = 5
    CATEGORY_ENVIRONMENT___AGRICULTURE = 6
    CATEGORY_KNOWLEDGE___TECHNOLOGY_TRANSFER = 7
    CATEGORY_POLICY___STANDARDS___ETHICS = 8

    CATEGORIES = [
        (CATEGORY_GREEN_ECONOMY, _('Green Economy')),
        (CATEGORY_ENERGY, _('Energy')),
        (CATEGORY_WATER___SANITATION, _('Water & Sanitation')),
        (CATEGORY_HEALTH, _('Health')),
        (CATEGORY_CONSTRUCTION___INFRASTRUCTURE, _('Construction & Infrastructure')),
        (CATEGORY_ENVIRONMENT___AGRICULTURE, _('Environment & Agriculture')),
        (CATEGORY_KNOWLEDGE___TECHNOLOGY_TRANSFER, _('Knowledge & Technology Transfer')),
        (CATEGORY_POLICY___STANDARDS___ETHICS, _('Policy, Standards, & Ethics')),
    ]

    category = models.IntegerField(choices=CATEGORIES)

    # Proposal Format
    # ~~~~~~~~~~~~~~~

    FORMAT_FULL_PAPER___PRESENTATION = 1
    FORMAT_POSTER = 2
    FORMAT_PROJECT = 3

    FORMATS = [
        (FORMAT_FULL_PAPER___PRESENTATION, _('Full Paper & Presentation')),
        (FORMAT_POSTER, _('Poster')),
        (FORMAT_PROJECT, _('Project')),
    ]

    format = models.IntegerField(choices=FORMATS)

    recording_release = models.BooleanField(
        default=True,
        help_text="By submitting your proposal, you agree to give permission to the conference organizers to record, edit, and release audio and/or video of your presentation. If you do not agree to this, please uncheck this box."
    )

    class Meta:
        verbose_name = "proposal"
