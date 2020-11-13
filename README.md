# eticket_cms

E-Ticket Content Management

### Tmux name: 
```
django_cms
```

```tmux
Start new named session:
tmux new -s [session name]

Detach from session:
ctrl+b d

List sessions:
tmux ls

Attach to named session:
tmux a -t [name of session]

Kill named session:
tmux kill-session -t [name of session]

Split panes horizontally:
ctrl+b "

Split panes vertically:
ctrl+b %

Kill current pane:
ctrl+b x

Move to another pane:
ctrl+b [arrow key]

Kill tmux server, along with all sessions:
tmux kill-server
```

### this is on main dir
``` 
conda create -n django_cms python=3.6 

sudo apt install python3-pip

. activate django_cms

pip3 install -r requirements.txt

python3.6 manage.py makemigrations

python3.6 manage.py migrate

python3.6 manage.py runserver 0.0.0.0:8001
```


### Clear Static files cache
```
python manage.py collectstatic --noinput --clear
```


### Add new Language

To add new language add following in `settings.py`:
```python
from django.conf import global_settings
import os

PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
LOCALE_PATHS = (
    os.path.join(PACKAGE_ROOT, 'locale'),
)

... 

LANGUAGES = (
    ## Customize this
    ...
    ('uz', gettext('uz')),

)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        ...
        , {
            'code': 'uz',
            'name': gettext('Uzbek'),
            'redirect_on_fallback': False,
            'public': True,
            'hide_untranslated': True,
        }
    ],
    ...
}

...

EXTRA_LANG_INFO = {
    'uz': {
        'bidi': False,  # right-to-left
        'code': 'uz',
        'name': 'Uzbek',
        'name_local': 'O\'zbek',  # unicode codepoints here
    },
}

# Add custom languages not provided by Django
import django.conf.locale


LANG_INFO = dict(django.conf.locale.LANG_INFO, **EXTRA_LANG_INFO)
django.conf.locale.LANG_INFO = LANG_INFO

# Languages using BiDi (right-to-left) layout
LANGUAGES_BIDI = global_settings.LANGUAGES_BIDI + ["uz"]
```

then open up a terminal and execute:

```python
python manage.py makemessages -l uz
```

> NOTE: open your locale>uz>LC_MESSAGES>django.po and check if "Plural-Forms" is as following:
`"Plural-Forms: nplurals=1; plural=0;\n"` if missing, please, add one.


```python
python manage.py compilemessages
```