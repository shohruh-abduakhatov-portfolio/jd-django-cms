# -*- coding: utf-8 -*-

####################################################################################################

import re

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


####################################################################################################


CLASS_NAME_FORMAT = re.compile(r'^\w[\w_-]*$')


class LanguageChooserModel(CMSPlugin):
    """
    A django CMS Plugin to use Lang Choose
    """

    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='+',
        parent_link=True,
    )

    label = models.CharField(
        _('label'),
        max_length=128,
        blank=True,
        help_text=_('Optional label for this plugin.'),
    )

    template = models.CharField(
        _('template'),
        max_length=50,
        blank=True)


    ##############################################

    def __str__(self):
        """ Instance's name shown in structure page """

        display = ''
        if self.label:
            display = '“{0}”: {1}'.format(self.label, display)
        return display
