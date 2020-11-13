# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from cms.models import CMSPlugin
from djangocms_attributes_field.fields import AttributesField


@python_2_unicode_compatible
class ListModel(CMSPlugin):
    label = models.CharField(blank=True, max_length=200, )
    extra_classes = models.CharField(blank=True, max_length=200, )
    id_name = models.CharField(max_length=50, blank=True, )
    attributes = AttributesField()


    def __str__(self):
        return self.label


@python_2_unicode_compatible
class ListItemModel(CMSPlugin):
    label = models.CharField(blank=True, max_length=200, )
    url_link = models.URLField(blank=True)
    link_title = models.CharField(blank=True, max_length=200, )
    text_body = models.CharField(blank=True, max_length=200, )
    extra_classes = models.CharField(blank=True, max_length=200, )
    id_name = models.CharField(max_length=50, blank=True, )
    attributes = AttributesField()


@python_2_unicode_compatible
class InlineTextModel(CMSPlugin):
    label = models.CharField(blank=True, max_length=200, )
    text_body = models.CharField(blank=True, max_length=200, )
    extra_classes = models.CharField(blank=True, max_length=200, )


    def __str__(self):
        return self.label
