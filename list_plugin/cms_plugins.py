# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class ListPlugin(CMSPluginBase):
    model = models.ListModel
    name = '<ul> List Plugin'
    render_template = 'list_plugin/list.html'
    parent_classes = []
    require_parent = False
    allow_children = True
    child_classes = []


    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


class ListItemPlugin(CMSPluginBase):
    model = models.ListItemModel
    name = '<li> item'
    render_template = 'list_plugin/list_item.html'
    require_parent = True
    allow_children = True
    parent_classes = []
    child_classes = []


class InlineTextPlugin(CMSPluginBase):
    model = models.InlineTextModel
    name = 'Simple Text'
    render_template = 'list_plugin/inline_text.html'


    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(ListPlugin)
plugin_pool.register_plugin(ListItemPlugin)
plugin_pool.register_plugin(InlineTextPlugin)
