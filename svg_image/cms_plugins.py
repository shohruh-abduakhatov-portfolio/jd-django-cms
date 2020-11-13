# -*- coding: utf-8 -*-

####################################################################################################

from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import CustomSvgImage


####################################################################################################

class CustomSvgImagePlugin(CMSPluginBase):
    model = CustomSvgImage
    name = _("Custom SVG Image <img>")
    render_template = "svg_image/plugin.html"
    parent_classes = []
    child_classes = []

    # Editor fieldsets
    fieldsets = (
        (None, {
            'fields': ('svg_image',
                       'height', 'width',
                       'alignment',
                       'alt_text')
        }),
        (_('Advanced Settings'), {
            'classes': ('collapse',),
            'fields': (
                'additional_class_names',
                'label',
                'id_name',
            ),
        }),
    )


####################################################################################################

plugin_pool.register_plugin(CustomSvgImagePlugin)
