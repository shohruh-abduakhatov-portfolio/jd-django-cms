# from django.conf.urls import url
#
# from . import views
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
from cms.apphook_pool import apphook_pool
from cms.appresolver import get_app_patterns
from cms.constants import SLUG_REGEXP
from django.conf import settings
from django.conf.urls import url

from login import views


if settings.APPEND_SLASH:
    regexp = r'^(?P<slug>%s)/$' % SLUG_REGEXP
else:
    regexp = r'^(?P<slug>%s)$' % SLUG_REGEXP

if apphook_pool.get_apphooks():
    urlpatterns = get_app_patterns()
else:
    urlpatterns = []

urlpatterns.extend([
    url(r'^logout/', views.sign_out),
    url(r'^check/', views.check_role),
    url(r'^$', views.auth, name='auth'),
])
