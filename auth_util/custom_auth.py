from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from auth_util.token import decode_token
from cms_panel.settings import SESSION_EXP, API_HEADERS


class CustomAuth(ModelBackend):

    def authenticate(self, request, username=None, password=None):
        token = request.GET.get('token')
        if token is None:
            return None
        decoded = decode_token(token)
        username = decoded['sub']

        try:
            user = User.objects.get(username=username)
            if not user.is_staff or not user.is_superuser or not user.is_active:
                return None
        except User.DoesNotExist:
            user = User(username=username)
            user.is_staff = True
            user.is_superuser = True
            user.save()
        request.session['token'] = token
        request.session.set_expiry(SESSION_EXP)
        return user


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


def get_headers(request):
    header = API_HEADERS
    header['Authorization'] = "Bearer {}".format(request.session.get('token'))
    header['X-FORWARDED-FOR'] = get_client_ip(request)
    header['User-Agent'] = request.META['HTTP_USER_AGENT']
    return header

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
