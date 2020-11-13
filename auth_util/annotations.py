from functools import wraps

from django.http import HttpResponseRedirect
from django.shortcuts import render



def check_session():
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            request = args[0]
            try:
                request.session['token']
                return f(*args, **kwargs)
            except KeyError:
                form = LoginUserForm()
                return render(request, 'login.html', {'form': form})


        return wrapped


    return decorator


def is_loged_in():
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            request = args[0]
            token = request.session.get('token')
            if token is None:
                token = request.GET.get('token')
            if token is not None and request.path is "/":
                request.session['token'] = token
                request.session.set_expiry(900)
                return HttpResponseRedirect('/user')

            return f(*args, **kwargs)


        return wrapped


    return decorator
