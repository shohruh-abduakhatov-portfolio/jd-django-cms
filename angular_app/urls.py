# from django.conf.urls import url
#
# from . import views
from django.contrib import admin
# from auth_app import views
#
#
# urlpatterns = [
#     url(r'^/', views.get, name='auth-login'),
# ]
# # urlpatterns = [
# #     url(r'^auth/', include('tinymce.urls')),
# # ]
# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url

from cms.apphook_pool import apphook_pool
from cms.appresolver import get_app_patterns
from cms.constants import SLUG_REGEXP

from angular_app import views


if settings.APPEND_SLASH:
    regexp = r'^(?P<slug>%s)/$' % SLUG_REGEXP
else:
    regexp = r'^(?P<slug>%s)$' % SLUG_REGEXP

if apphook_pool.get_apphooks():
    urlpatterns = get_app_patterns()
else:
    urlpatterns = []

urlpatterns.extend([
    url(r'^ticket/', views.train_search, name='train_search'),
    # url(r'^lang/', views.change_lang, name='get'),
])
