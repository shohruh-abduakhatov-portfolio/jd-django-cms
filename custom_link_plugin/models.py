# -*- coding: utf-8 -*-

####################################################################################################

import re

from cms.models import CMSPlugin
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


####################################################################################################
from djangocms_attributes_field.fields import AttributesField


CLASS_NAME_FORMAT = re.compile(r'^\w[\w_-]*$')


class CustomLinkImage(CMSPlugin):
    """
    A django CMS Plugin to use Custom Link/Button
    """

    TAG_TYPE_CHOICES = (
        ('a', 'a'),
        ('button', 'button'),
        ('span', 'span'),
        ('div', 'div'),
        ('input', 'input'),
        ('label', 'label'),
        ('ul', 'ul'),
        ('ol', 'ol'),
        ('li', 'li'),
        ('form', 'form'),
    )

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
    body_text = models.CharField(
        _('text'),
        max_length=512,
        blank=True,
        help_text=_('Text Body (Optional)'),
    )

    id_name = models.CharField(
        _('id name'),
        max_length=50,
        blank=True, )

    tag_type = models.CharField(
        verbose_name=_('tag Type'),
        max_length=50,
        choices=TAG_TYPE_CHOICES,
        default=TAG_TYPE_CHOICES[0][0],
    )

    additional_class_names = models.TextField(
        verbose_name=_('additional classes'),
        blank=True,
        help_text=_('Comma separated list of additional classes to apply to tag_type'),
    )

    width = models.PositiveIntegerField(_("width"), null=True, blank=True)
    height = models.PositiveIntegerField(_("height"), null=True, blank=True)

    attributes = AttributesField()

    ##############################################

    def __str__(self):

        """ Instance's name shown in structure page """

        display = ''
        if self.additional_class_names:
            display = '{0} ({1})'.format(display, self.additional_class_names)
        if self.label:
            display = '“{0}”: {1}'.format(self.label, display)
        return display


    ##############################################

    def clean(self):

        if self.additional_class_names:
            additional_class_names = list(html_class.strip()
                                          for html_class in self.additional_class_names.split(','))
            for class_name in additional_class_names:
                class_name = class_name.strip()
                if not CLASS_NAME_FORMAT.match(class_name):
                    raise ValidationError(
                        _('"{0}" is not a proper css class name.').format(class_name))
            self.additional_class_names = ', '.join(set(additional_class_names))


    ##############################################

    @property
    def get_additional_class_names(self):

        if self.additional_class_names:
            # Removes any extra spaces
            return ' '.join((html_class.strip()
                             for html_class in self.additional_class_names.split(',')))
        else:
            return ''
