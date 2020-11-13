# -*- coding: utf-8 -*-

####################################################################################################

from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import CustomLinkImage


####################################################################################################

class CustomLinkPlugin(CMSPluginBase):
    model = CustomLinkImage
    name = _("Custom Link / Button")
    render_template = "custom_link_plugin/link_button.html"
    allow_children = True
    require_parent = False
    parent_classes = []
    child_classes = []

    # Editor fieldsets
    fieldsets = (
        (None, {
            'fields': (
                'tag_type',
                'body_text',
                'height', 'width',
            )
        }),
        (_('Advanced Settings'), {
            'classes': ('collapse',),
            'fields': (
                'additional_class_names',
                'label',
                'id_name',
                'attributes',
            ),
        }),
    )


####################################################################################################

plugin_pool.register_plugin(CustomLinkPlugin)
