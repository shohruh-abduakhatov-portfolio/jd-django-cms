import json

import requests
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse, JsonResponse, \
    HttpResponseServerError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from auth_util.custom_auth import get_headers
from cms_panel.settings import DJANGO_URL, API_HEADERS, MIDDLEWARE_URL
from login.utils import ACCESS_PAGES, UNIFORM


def sign_out(request):
    token = request.GET.get('token')
    if token is None:
        return HttpResponseBadRequest("Token needed")

    header = get_headers(request)
    header['Authorization'] = 'Bearer ' + token

    server_response = requests.post(MIDDLEWARE_URL + "users/logout", headers=header)
    try:
        body = json.loads(server_response.content.decode())
        if body is None or body is False:
            return HttpResponseServerError()
    except:
        pass

    response = HttpResponseRedirect('/')
    try:
        request.session.flush()
        response.delete_cookie('token')
        response.delete_cookie('csrftoken')
    except:
        pass
    logout(request)
    return response


def auth(request):
    # todo add IP check here
    user = authenticate(request)
    if user is None:
        url = DJANGO_URL
        token = request.GET.get('token')
        if token is not None:
            url += "?token=" + token
        return redirect(url)
    login(request, user)
    return redirect('/admin')


def check_role(request):
    if 'HTTP_AUTHORIZATION' in request.META:
        auth = request.META['HTTP_AUTHORIZATION']
        token = request.META['HTTP_AUTHORIZATION'].split(" ")[1]
        lang = request.GET.get('lang')

        if token is None or lang is None:
            return HttpResponseBadRequest()
        # header = API_HEADERS
        # header['Authorization'] = auth
        header = get_headers(request)
        header['Authorization'] = 'Bearer ' + token
        role_response = requests.post(MIDDLEWARE_URL + "users/check/token", headers=header)
        role = json.loads(role_response.content.decode())
        role_pages = ACCESS_PAGES[role[0]]
        role_pages_response = {}
        try:
            role_pages_response['url'] = role_pages['url']
            role_pages_response[lang] = role_pages[lang]
        except KeyError:
            role_pages_response = {'url': [], lang: []}
        role_pages_response['url'] = role_pages_response['url']+UNIFORM['logout']['url']
        role_pages_response[lang] = role_pages_response[lang]+UNIFORM['logout'][lang]
        return JsonResponse(role_pages_response)

















