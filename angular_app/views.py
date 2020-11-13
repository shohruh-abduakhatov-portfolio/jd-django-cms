from urllib.parse import urlencode

from django.http import HttpResponseRedirect

from django.shortcuts import redirect

from cms_panel.settings import ANGULAR_API, DJANGO_URL


def train_search(request):
    # https://railway.uz/?f=2030134&t=2060027&date=04/03/2019
    f = request.GET.get('f')
    t = request.GET.get('t')
    date = request.GET.get('date')
    date2 = request.GET.get('date2')
    token = request.session.get('token')
    params_dict = {
        't': t,
        'f': f,
        'date': date,
    }
    if date2 is not None: params_dict['date2'] = date2
    if token is None:
        request.COOKIES.get('token')
    else:
        params_dict['token'] = token
    params = urlencode(params_dict).replace('%2F', '.')
    response = ANGULAR_API + "process/train/?" + params
    return HttpResponseRedirect(response)
