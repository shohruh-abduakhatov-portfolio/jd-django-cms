# -*- coding: utf-8 -*-

####################################################################################################

from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import LanguageChooserModel


####################################################################################################

class LanguageChooserPlugin(CMSPluginBase):
    model = LanguageChooserModel
    name = _("Languge chooser")
    render_template = "language_plugin/language_chooser.html"
    allow_children = True
    require_parent = False
    parent_classes = []
    child_classes = []

    # Editor fieldsets
    fieldsets = (
        (None, {
            'fields': (
                'template',
            )
        }),
        (_('Advanced Settings'), {
            'classes': ('collapse',),
            'fields': (
                'label',
            ),
        }),
    )


####################################################################################################

plugin_pool.register_plugin(LanguageChooserPlugin)
